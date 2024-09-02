from django import forms
from employee.models import Position

class EmployeeForm(forms.Form):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
        ("LGBT", "LGBT")
    )
    first_name = forms.CharField(max_length=155)
    last_name = forms.CharField(max_length=155)
    gender = forms.ChoiceField(choices=GENDER)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    salary = forms.DecimalField(max_digits=10, decimal_places=2)
    position = forms.ModelChoiceField(
        queryset=Position.objects.all()
    )