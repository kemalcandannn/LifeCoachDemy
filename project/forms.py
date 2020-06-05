from django import forms
from django.forms import DateTimeInput

from .models import Project


class DateTimeInput(DateTimeInput):
    input_type = 'datetime'

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'name',
            'content',
            'documentation',
            'price',
            'deadline',
            'done',
        ]
        widgets = {
            'deadline': DateTimeInput()
        }
