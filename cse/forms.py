from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['sid', 'name', 'branch', 'subject']
        # widgets = {
        #     'branch': forms.Select(choices=Student.select_branch),
        #     'subject': forms.Select(choices=Student.select_subject),
        # }
