# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import get_template
from datetime import date
import re

#from microdetector import detect_mobile

todaydate = date.today()

overview = '''
    I am a software and systems engineer with experience in the Internet, streaming media, and visual effects production industries. My experience centers on bringing high performance computing and systems integration for digital media content production and delivery. My interests are systems integration and design, cloud computing, streaming media, development of systems provisioning tools and automation, and configuration of interfaces for data analysis and visualization. I enjoy researching emerging technologies and employing holistic analysis to solve problems in a forward-thinking manner.
'''

def projects(request):


    harvardOverview = """
        The distance education project is a prototypical model that I designed for the post- production and delivery of high quality digital media over high-speed data networks and the Internet. The implementation of this model represents an initiative for a standard system architecture that would allow Harvard University Division of Continuing Education to promote and continue development in Distance Education technologies over the Internet as well its expansion.
    """

    disneyOverview = """
        Image Movers Digital is a division of the Walt Disney Studios run by Director Robert Zemeckis which specializes in the production of animated films employing motion capture and digital film technology in stereoscopic format (also known as 3D). My work at the studio focused on systems infrastructure development and integration and on the production side, the building of tools and shot work support for visual effects artists.
    """

    garrickOverview = """
        Garrick is an original short fictional narrative composed by live-action performance captured on high definition (HD) video conveyed with CGI and classical animation. The main goal of the project is to develop photo realistic virtual environments and their integration with live action. The project also covers the development of workflows in both production and post-production for the automation of rendering processes.
    """

    cbsInteractive = """
        CBS Interactive ( formerly CBS Digital Media Group), a division of CBS corporation, is an online content network for information and entertainment. Brands include CBS.com, CNET, TV.com, metacritic.com, and CBS News.
        My role at CBS Interactive is as an engineering generalist currently working for TV.com where assist and support  in the integration and implementation of back-end web services,  front-end applications, and development of Web applications for content management systems for online publishing, and automation of content acquisition.
        On the front-end side, my work has focused on developing Web applications for content management systems employing technologies like Ajax, jQuery, HTML5, CSS, django apps, JavaScript, Twittter Bootstrap, and REST services integration.   An important component of this task also include automation of content acquisition and data consumption from RSS feeds from Television partners.
        On the back-end side, my work has mainly focused on integrations and configurations of services on AWS/Right Scale. Specifically my contributions in this are have been the configuration of Web servers, building of server templates, CDN integrations, configuration of Web apps Django applications,  URL dispatchers and  redirects, Tomcat/J2EE services, and caching ( memcached).
    """

    project =  request.GET["project"]

    if re.match(project, "cbsinteractive"):
        template = get_template('projects/cbsinteractive.html')
        variables = Context({
            'head_title': 'Antonio A Eggermont Web Site',
            'page_title': 'My Work @ CBS Interactive',
            'page_name' : 'antonioeggermont.com',
            'project_description' : cbsInteractive,
        })

        output = template.render(variables)
        return HttpResponse(output)

    elif re.match(project, "disney"):
        template = get_template('projects/disney.html')

        variables = Context({
            'head_title': 'Antonio A Eggermont Web Site',
            'page_title': 'My Work @ CBS Interactive',
            'page_name' : 'antonioeggermont.com',
            'project_description' : disneyOverview,
        })

        output = template.render(variables)
        return HttpResponse(output)


    elif re.match(project, "harvard"):

        template = get_template('projects/harvarddistancedd.html')

        variables = Context({
            'head_title': 'Antonio A Eggermont Web Site',
            'page_title': 'My Work @ CBS Interactive',
            'page_name' : 'antonioeggermont.com',
            'project_description' : harvardOverview,
        })

        output = template.render(variables)
        return HttpResponse(output)


    elif re.match(project, "garick"):

        template = get_template('projects/garrick.html')
        variables = Context({
            'head_title': 'Antonio A Eggermont Web Site',
            'page_title': 'My Work @ CBS Interactive',
            'page_name' : 'antonioeggermont.com',
            'project_description' : garrickOverview,
        })

        output = template.render(variables)
        return HttpResponse(output)

    else:
        response_html = u"<html><body><h1> Project not found </h1>  </body></html>"
        return HttpResponse(response_html)



def references(request):

    template = get_template('home/references.html')

    variables = Context({
        'head_title': 'Antonio A Eggermont Web Site',
        'page_title': 'References',
        'page_overview': overview,
        'today_date': todaydate,
        'page_name' : 'antonioeggermont.com'
    })

    output = template.render(variables)
    return HttpResponse(output)


def contact(request):

    template = get_template('home/contact.html')

    variables = Context({
        'head_title': 'Antonio A Eggermont Web Site',
        'page_title': 'Contact',
        'page_overview': overview,
        'today_date': todaydate,
        'page_name' : 'antonioeggermont.com'
    })

    output = template.render(variables)
    return HttpResponse(output)


def resume(request):

    template = get_template('home/resume.html')

    variables = Context({
        'head_title': 'Antonio A Eggermont Web Site',
        'page_title': 'My Resume',
        'page_overview': overview,
        'today_date': todaydate,
        'page_name' : 'antonioeggermont.com'
    })

    output = template.render(variables)
    return HttpResponse(output)

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


def healthcheck(request):

    response_html = u"<html><body></body></html>"
    return HttpResponse(response_html)


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


