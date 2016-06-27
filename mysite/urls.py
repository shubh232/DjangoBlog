from django.conf.urls import patterns, include, url
from django.contrib import admin

from mysite.views import Index,Check

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^check/$',Check.as_view(),name = 'check')
    url(r'^admin/', include(admin.site.urls)),
)



