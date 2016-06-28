from django.shortcuts import render
from django.views.generic import CreateView
from loguser.forms import RegForm

class Regis(CreateView):
    form_class = RegForm
    template_name = 'register.html'
    success_url = '/'

