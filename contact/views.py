from django import forms
from django.shortcuts import render
from django.views.generic import CreateView,View
from .forms import ContactForms
from .models import *


class ContactView(View):
    def get(self,request):
        contacts = ContactLink.objects.all()
        form = ContactForms()
        return render(request,'contact/contact.html',{"contacts":contacts, "form":form})


class CreateContact(CreateView):
    form_class = ContactForms
    success_url = '/'



class AboutView(View):
    def get(self,request):
        about = About.objects.last()
        return render(request,'contact/about.html',{"about":about})