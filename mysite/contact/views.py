# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template

cont = " Antonio.Eggermont@post.harvard.edu "


def contact(request):
    template = get_template('contact/contact.html')
    
    variables = Context({
        'head_title': 'My contact information',
        'page_title': 'My contact information',
        'page_overview': cont ,
        })

    output = template.render(variables)
    return HttpResponse(output)


