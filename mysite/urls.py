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
    (r'^enabled.html$', 'mysite.home.views.healthcheck'),
    (r'^contact/', 'mysite.home.views.contact'),
    (r'^references/', 'mysite.home.views.references'),
    (r'^resume/', 'mysite.home.views.resume'),
    (r'^garick/', 'mysite.home.views.garrick'),
    (r'^feeders/', 'mysite.home.views.feeder'),
    (r'^cookies/', 'mysite.home.views.cookies'),
    (r'^addContactInfo/', 'mysite.contact.views.addContactInfo'),
    (r'^photoAlbums/', 'mysite.home.views.photoAlbums'),

    ###  MOBILE SITE ###
    (r'^m/', 'mysite.home.views.mobilehome'),
    (r'^test', 'mysite.home.views.test'),

    ### Off-sitre links redirection ###
    (r'^redir$', 'mysite.home.views.offsiteRedirect'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': (os.path.join(PROJECT_PATH, 'static')) }),
    (r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root': (os.path.join(PROJECT_PATH, 'public')) }),
    url(r'^projects$', 'mysite.home.views.projects'),
    #url(r'^$', ExampleView.as_view(), name='example-resource'),
    #url(r'^(?P<num>[0-9]+)/$', AnotherExampleView.as_view(), name='another-example'),  
)
