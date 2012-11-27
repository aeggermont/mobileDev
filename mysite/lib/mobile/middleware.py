
import re
from django.http import HttpResponseRedirect, Http404
from urlparse import urlparse,  urlunparse
from django.core.urlresolvers import resolve
import logging

class MobileMiddleware(object):
    """
    Middleware class to check the user agent per request and set a request level variable
    if the user is using a mobile browser
    """

    def process_request(self, request):
        """
        One each request, the request object is tested to see if its mobile.
        """
        print "Introspecting user agents:"
        print request.META.get('HTTP_USER_AGENT', "")