from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'name',
            'content',
            'documentation',
            'lower_price',
            'upper_price',
            'deadline',

        ]
