# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template


def home(request):
    return render_to_response("home/index.html")



def testView(request):
    site_name = "My Site"
    response_html = u"<html<<body> Welcome to %s. </body></html>" % site_name
    return HttpResponse(response_html)
     
