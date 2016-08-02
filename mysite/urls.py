from django.conf.urls import patterns, include, url
from django.contrib import admin
from loguser.views import Regis,NewArt,Landing,AllPosts,ArticleView
from mysite.views import Index , Check
from django.views.generic import TemplateView
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^reg/$',Regis.as_view(),name='register'),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^check/',Check.as_view(),name='check'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',login,{'template_name': 'login1.html'}),
    url(r'^accounts/profile/allposts/(?P<slug>[^/]+)/$', ArticleView.as_view()),
    url(r'^accounts/profile/$',login_required(Landing.as_view())),
    url(r'^accounts/profile/allposts/$',login_required(AllPosts.as_view()),name='allposts'),
    url(r'^accounts/profile/newart/$',login_required(NewArt.as_view())),
    url(r'^accounts/profile/logout/$',logout,{'next_page':'/login/'})
)



