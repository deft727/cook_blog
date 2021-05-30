from django import forms
from django.db import models
from django.forms import fields
from .models import ContactModel


class ContactForms(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'