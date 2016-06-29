from django.conf.urls import patterns, include, url
from django.contrib import admin
from loguser.views import Regis,NewArt
from mysite.views import Index , Check
from django.views.generic import TemplateView
from django.contrib.auth.views import login
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^reg/$',Regis.as_view(),name='register'),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^check/',Check.as_view(),name='check'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',login,{'template_name': 'login.html'}),
    url(r'^accounts/profile/$',TemplateView.as_view(template_name='profile.html')),
    url(r'^accounts/profile/newart/$',NewArt.as_view()),
)



