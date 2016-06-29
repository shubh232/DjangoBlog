
from django.views.generic import CreateView,FormView,TemplateView
from loguser.forms import RegForm,ArticleForm
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
class Regis(CreateView):
    form_class = RegForm
    template_name = 'register.html'
    success_url = '/login/'

class NewArt(CreateView):
    form_class = ArticleForm
    template_name = 'newart.html'
    success_url = '/profile/'
