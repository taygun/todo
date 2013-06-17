from django.conf.urls import patterns, include, url
from django.contrib import admin
from todo.models import Task
from todo import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^todo/', include('todo.foo.urls')),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'index.html'}),
    url(r'^index', 'todo.views.index', name='index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
