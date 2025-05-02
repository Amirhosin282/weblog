from django import forms
from .models import Messeage

class ContactForm(forms.ModelForm):
    class Meta:
        model = Messeage
        fields = ['name', 'email_addr', 'phone_number', 'message']