from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import patterns, url
from django.conf import settings
import os
from django.http import HttpResponseRedirect


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))


urlpatterns = patterns('',
    (r'^$', 'mysite.home.views.home'),
    (r'^biography/', 'mysite.home.views.biography'),
    #(r'^preview/', 'mysite.testsite.views.home'),
    #(r'^viderob/', 'mysite.videorobot.views.home'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': (os.path.join(PROJECT_PATH, 'static')) }),
    (r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root': (os.path.join(PROJECT_PATH, 'public')) }),

    #url(r'^$', ExampleView.as_view(), name='example-resource'),
    #url(r'^(?P<num>[0-9]+)/$', AnotherExampleView.as_view(), name='another-example'),  
)
