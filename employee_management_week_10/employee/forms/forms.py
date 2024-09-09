from django import forms
from employee.models import Employee, EmployeeAddress, Department, Position, Project  # Only import models

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'gender', 'birth_date', 'hire_date', 'salary', 'position']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_hire_date(self):
        import datetime

        cleaned_data = super().clean()
        hire_date = cleaned_data.get("hire_date")
        if not hire_date:
            self.add_error("hire_date", "Hire date is required")
        elif hire_date > datetime.date.today():
            self.add_error("hire_date", "Hire date cannot be a future date")
        return hire_date
    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'manager', 'due_date', 'start_date', 'description']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'staff': forms.SelectMultiple()
        }

    def clean_start_date(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")
        if start_date > due_date:
            self.add_error("start_date", "Start date cannot be greater than due date")
        return start_date
    
class ProjectDetailForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'manager', 'due_date', 'start_date', 'description', 'staff']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'staff': forms.SelectMultiple()
        }

    def clean_start_date(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")
        if start_date > due_date:
            self.add_error("start_date", "Start date cannot be greater than due date")
        return start_date