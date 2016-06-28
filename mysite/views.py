from django.views.generic import View
from django.http import HttpResponse
from django import get_version
from django.shortcuts import render
class Check(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Running Django ' + str(get_version()) + " on Shubh")

class Index(View):

    def get(self, request, *args, **kwargs):
        return render(request,template_name='index.html')
        # return HttpResponse('Running Django ' + str(get_version()) + " on OpenShift")
#