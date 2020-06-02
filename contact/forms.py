from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'full_name',
            'name',
            'eMail',
            'content',
        ]

class ContactUpdateForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'answered',
        ]
