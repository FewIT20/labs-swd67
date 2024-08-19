from django.shortcuts import render
from .models import Employee, Position, Project
from django.views import View
from django.http import JsonResponse, HttpResponse

class ViewEmployee(View):

    def get(self, request):
        employees = Employee.objects.all()
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
        from django.db.models import F, Value
        from django.db.models.functions import Concat

        project = Project.objects.annotate(
            full_name=Concat(F('manager__first_name'), Value(' '), F('manager__last_name'))
        ).get(id=id)
        staff = project.staff.filter(project=project)

        start_date = project.start_date.strftime("%Y-%m-%d") 
        end_date = project.due_date.strftime("%Y-%m-%d")
        context = {
            'project': project,
            'start_date': start_date,
            'end_date': end_date,
            'staffs': staff
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
        