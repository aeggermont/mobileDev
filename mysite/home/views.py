# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import get_template
from datetime import date
from django.http import Http404
from django import forms
import datetime
from django.core.context_processors import csrf


import json


import re
from django.conf import settings as setting

#from microdetector import detect_mobile

todaydate = date.today()

overview = '''
    I am a software and systems engineer with experience in the Internet, streaming media, and visual effects production industries. My experience centers on bringing high performance computing and systems integration for digital media content production and delivery. My interests are systems integration and design, cloud computing, streaming media, development of systems provisioning tools and automation, and configuration of interfaces for data analysis and visualization. I enjoy researching emerging technologies and employing holistic analysis to solve problems in a forward-thinking manner.
'''


def photoAlbums(request):

    template = get_template('projects/photoalbums.html')

    variables = Context({
        'head_title': 'Antonio A Eggermont Web Site',
        'page_title': 'Photo Albums',
        'page_name' : 'antonioeggermont.net'
    })

    output = template.render(variables)
    return HttpResponse(output)

    #response_html = u"<html><body><h1> Photo Album  </h1> </body></html>"
    #return HttpResponse(response_html)


def addContactInfo(request):


    items = [10,20,30,50,100]

    myfeed = { "service" : "httpd",
               "lastupdate" : str(datetime.datetime.now()),
               "items" : items
    }


    if request.method == 'GET':
        return HttpResponse(json.dumps(myfeed))

    elif request.method == 'POST':

        print request
        response_html = u"<html><body><h1> Getting a POST Request </h1> </body></html>"
        return HttpResponse(response_html)

    else:
        response_html = u"<html><body><h1> Invalid Request </h1> </body></html>"
        return HttpResponse(response_html)



def test(request):

    template = get_template('home/test1.html')

    variables = Context({
        'head_title': 'Antonio A Eggermont Web Site',
        'page_title': 'AJAX Test Page',
        'page_name' : 'antonioeggermont.net'
    })

    output = template.render(variables)
    return HttpResponse(output)





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
            'page_name' : 'antonioeggermont.net',
            'project_description' : cbsInteractive,
        })

        output = template.render(variables)
        return HttpResponse(output)

    elif re.match(project, "disney"):
        template = get_template('projects/disney.html')

        variables = Context({
            'head_title': 'Antonio A Eggermont Web Site',
            'page_title': 'My Work @ CBS Interactive',
            'page_name' : 'antonioeggermont.net',
            'project_description' : disneyOverview,
        })

        output = template.render(variables)
        return HttpResponse(output)


    elif re.match(project, "harvard"):

        template = get_template('projects/harvarddistancedd.html')

        variables = Context({
            'head_title': 'Antonio A Eggermont Web Site',
            'page_title': 'My Work @ CBS Interactive',
            'page_name' : 'antonioeggermont.net',
            'project_description' : harvardOverview,
        })

        output = template.render(variables)
        return HttpResponse(output)


    elif re.match(project, "garick"):

        template = get_template('projects/garrick.html')
        BASE_IMAGE_PATH = setting.BASE_IMAGE_PATH + "/carousel/"
        imageSequence = []

        compFrames    = map(lambda x: ''.join([BASE_IMAGE_PATH, "GarrickPic_" + ("0" + str(x) if x < 10 else str(x)) + ".jpg"]) ,range(1,23))
        greenScFrames = map(lambda x: ''.join([BASE_IMAGE_PATH, "GarrickPicGreen_" + ("0" + str(x) if x < 10 else str(x)) + ".jpg"]) ,range(1,13))

        # for image in compFrames:
        #    imageSequence.append(image)
        #    print compFrames.index()

        # print imageSequence


        # files = [{'name': file.split("/")[-1],
        #      'path': ''.join([BASE_IMAGE_PATH, file]),
        #      'file': file,
        #      'cdn_path': ''.join([BASE_IMAGE_PATH, file]) } for file in files]

        variables = Context({
            'head_title': 'Antonio A Eggermont Web Site',
            'page_title': 'Garrick, Digital Cinematography',
            'today_date': todaydate,
            'compFrames' : compFrames,
            'greenScFrames' : greenScFrames,
            'page_name' : 'antonioeggermont.net'
        })

        return HttpResponse(template.render(variables))

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
        'page_name' : 'antonioeggermont.net'
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
        'page_name' : 'antonioeggermont.net'
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
        'page_name' : 'antonioeggermont.net'
    })

    output = template.render(variables)
    return HttpResponse(output)




class ContactForm(forms.Form):
    name    = forms.CharField(label="Your name: ", max_length=40)
    sender = forms.EmailField(label="Your email address")
    message = forms.CharField(label="Leave a message: ", widget=forms.Textarea ,  max_length=300)
    cc_myself = forms.BooleanField(required=False)




def biography(request):
    """
    :param request: GET
    :return: Form object for contact info saver, todays date, etc
    """

    if request.method == 'GET':

        # Unbound form
        form = ContactForm()

        template = get_template('home/biography.html')
        myHomeImages = { '1' : 'GarrickPic_01.jpg', '2' : 'GarrickPic_02.jpg', '3' :  'GarrickPic_03.jpg' }

        print "Hello world!"

        context = {
            'request'   : request,
            'form'      : form,
            'today_date': todaydate,
            'head_title': 'Antonio Aranda Eggermont Web Site',
            'page_title': 'Welcome to my site',
            'page_name' : 'antonioeggermont.net',

        }

        context.update(csrf(request))
        return render_to_response('home/biography.html', context)






def healthcheck(request):

    response_html = u"<html><body></body></html>"
    return HttpResponse(response_html)


def garrick(request):

    template = get_template('projects/garrick.html')

    BASE_IMAGE_PATH = setting.BASE_IMAGE_PATH + "/carousel/"

    compFrames    = map(lambda x: ''.join([BASE_IMAGE_PATH, "GarrickPic_" + ("0" + str(x) if x < 10 else str(x)) + ".jpg"]) ,range(1,13))
    greenScFrames = map(lambda x: ''.join([BASE_IMAGE_PATH, "GarrickPicGreen_" + ("0" + str(x) if x < 10 else str(x)) + ".jpg"]) ,range(1,13))

    # files = range(1, 13)[GarrickPic_01.jpg]
    # files = [{'name': file.split("/")[-1],
    #      'path': ''.join([BASE_IMAGE_PATH, file]),
    #      'file': file,
    #      'cdn_path': ''.join([BASE_IMAGE_PATH, file]) } for file in files]

    variables = Context({
        'head_title': 'Antonio A Eggermont Web Site',
        'page_title': 'Garrick, Digital Cinematography',
        'today_date': todaydate,
        'compFrames' : compFrames,
        'greenScFrames' : greenScFrames,
        'page_name' : 'antonioeggermont.net'
    })

    return HttpResponse(template.render(variables))


def feeder(request):

    items = [10,20,30,50,100]

    myfeed = { "service" : "httpd",
               "lastupdate" : str(date.today()),
               "items" : items
            }


    response_html = json.dumps(myfeed)
    return HttpResponse("Hello there!")



def cookies(request):

    template = get_template('home/testCookies.html')

    variables = Context({
        'page_title': 'Testing Cookies',
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
        'page_name' : 'antonioeggermont.net'
        })

    output = template.render(variables)
    return HttpResponse(output)




def mobilehome(request):


    template = get_template('home/home.html')
    myHomeImages = { '1' : 'GarrickPic_01.jpg', '2' : 'GarrickPic_02.jpg', '3' :  'GarrickPic_03.jpg' }

    variables = Context({
        'head_title': 'Antonio A Eggermont Web Site',
        'page_title': 'Welcome to my site',
        'page_overview': overview,
        'today_date': todaydate,
        'page_name' : 'antonioeggermont.net'
    })

    output = template.render(variables)
    return HttpResponse(output)


def offsiteRedirect(request):
    """Redirection for offsite links"""

    url = request.GET.get('url')
    if not url:
        raise Http404

    return HttpResponseRedirect(urllib.unquote_plus(url))