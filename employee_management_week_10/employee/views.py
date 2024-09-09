from django.shortcuts import render, redirect
from .models import Employee, Position, Project
from .forms import forms
from django.views import View
from django.http import JsonResponse, HttpResponse

class ViewProjectCreate(View):

    def get(self, request):
        context = {
            'forms': forms.ProjectForm()
        }
        return render(request, 'project_form.html', context)

    def post(self, request):
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project")
        context = {
            'forms': form 
        }
        return render(request, 'project_form.html', context)

class UpdateProject(View):
    
    def post(self, request, id):
        project = Project.objects.get(id=id)
        form = forms.ProjectDetailForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        return HttpResponse("error")

class ViewCreateEmployee(View):

    def get(self, request):
        context = {
            'forms': forms.EmployeeForm()
        }
        return render(request, 'employee_form.html', context)
    
    def post(self, request):
        form = forms.EmployeeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            employee = Employee(
                first_name=data["first_name"],
                last_name=data["last_name"],
                gender=data["gender"],
                birth_date=data["birth_date"],
                hire_date=data["hire_date"],
                salary=data["salary"],
                position=data["position"]
            )
            employee.save()
            return redirect("employee")  # Redirect to the desired page after successful submission
        context = {
            'forms': form 
        }
        return render(request, 'employee_form.html', context)   

class ViewEmployee(View):

    def get(self, request):
        employees = Employee.objects.all().order_by("-hire_date")
        context = {
            'employees': employees,
            'total': employees.count()
        }
        return render(request, 'employee.html', context)

class ViewLayout(View):

    def get(self, request):
        return render(request, 'layout.html')

class ViewPosition(View):

    def get(self, request):
        from django.db.models import Count
        positions = Position.objects.annotate(employee_total = Count("employee")).order_by("id")
        context = {
            'positions': positions
        }
        return render(request, 'position.html', context)
    
class ViewProject(View):

    def get(self, request):
        projects = Project.objects.all()
        context = {
            'projects': projects
        }
        return render(request, 'project.html', context)
    
class ViewProjectDetail(View):

    def get(self, request, id):
        project = Project.objects.get(id=id)
        form = forms.ProjectDetailForm(instance=project)
        staffs = project.staff.all()
        context = {
            'project': project,
            'staffs': staffs,
            'forms': form
        }
        return render(request, 'project_details.html', context)

    def delete(self, request, id):
        import json
        body = json.loads(request.body.decode('utf-8'))
        if body['action'] == "deleteProject":
            project = Project.objects.get(id=id)
            if not project:
                return HttpResponse(status=404)
            project.delete()
            return JsonResponse({'message': 'Project has been deleted!'})
        elif body['action'] == "removeStaff":
            project = Project.objects.get(id=id)
            staff_id = body['emp_id']
            staff = Employee.objects.get(id=staff_id)
            if not project or not staff:
                return HttpResponse(status=404)
            project.staff.remove(staff)
            return JsonResponse({'message': 'Staff has been removed!'})

    def put(self, request, id):
        import json
        body = json.loads(request.body.decode('utf-8'))
        staff_id = body['emp_id']
        project = Project.objects.get(id=id)
        staff = Employee.objects.get(id=staff_id)
        if not project or not staff:
            return HttpResponse(status=404)
        project.staff.add(staff)
        return JsonResponse({'message': 'Staff has been added!'})
        