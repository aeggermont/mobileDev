# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template
from datetime import date

todaydate = date.today()

overview = '''
I am a software and systems engineer with experience in the Internet, streaming media, and visual effects production industries. My experience centers on bringing high performance computing and systems integration for digital media content production and delivery. My interests are systems integration and design, cloud computing, streaming media, development of systems provisioning tools and automation, and configuration of interfaces for data analysis and visualization. I enjoy researching emerging technologies and employing holistic analysis to solve problems in a forward-thinking manner. 
'''

def biography(request):

    template = get_template('home/biography.html')
    myHomeImages = { '1' : 'GarrickPic_01.jpg', '2' : 'GarrickPic_02.jpg', '3' :  'GarrickPic_03.jpg' }

    variables = Context({
        'head_title': 'Antonio A Eggermont Web Site',
        'page_title': 'Welcome to my site',
        'page_overview': overview,
        'today_date': todaydate,
        'page_name' : 'antonioeggermont.com'
    })

    output = template.render(variables)
    return HttpResponse(output)



def home(request):

    # response_html = u"<html><body><h1> Getting a GET request </h1> </body></html>"
    # return HttpResponse(response_html)


    template = get_template('home/home.html')
    myHomeImages = { '1' : 'GarrickPic_01.jpg', '2' : 'GarrickPic_02.jpg', '3' :  'GarrickPic_03.jpg' }  
 
    variables = Context({
        'head_title': 'Antonio A Eggermont Web Site',
        'page_title': 'Welcome to my site',
        'page_overview': overview,
        'today_date': todaydate,
        'page_name' : 'antonioeggermont.com'
        })

    output = template.render(variables)
    return HttpResponse(output)


