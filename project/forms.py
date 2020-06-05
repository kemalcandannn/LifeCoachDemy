from django import forms
from django.forms import DateInput

from .models import Project


class DateInput(DateInput):
    input_type = 'date'

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
            'deadline': DateInput()
        }
