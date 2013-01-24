from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import Context
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import get_template
from datetime import date
from django.http import Http404
from django import forms
import datetime
import smtplib
from django.core.context_processors import csrf


class ContactForm(forms.Form):

    message = forms.CharField()
    name    = forms.CharField()
    email   = forms.CharField()


def addContactInfo(request):

    items = [10,20,30,50,100]

    myfeed = { "service" : "httpd",
               "lastupdate" : str(datetime.datetime.now()),
               "items" : items
    }


    if request.method == 'GET':
        return HttpResponse(json.dumps(myfeed))

    elif request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            name    = form.cleaned_data.get('name')
            email   = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            sendEmail(name, email, message)


            context = {
                'request'   : request,
                'head_title': 'Antonio Aranda Eggermont Web Site',
                'page_title': 'About Me',
                'page_name' : 'antonioeggermont.net',
                'contact_info': True,

                }

            #return HttpResponseRedirect('/biography/')
            #return HttpResponse(response_html)
            context.update(csrf(request))
            return render_to_response('home/biography.html', context)

        else:
            response_html = u"<html><body><h1> uhmmm something went wrong...  </h1> </body></html>"
            return HttpResponse(response_html)
    else:
        response_html = u"<html><body><h1> Invalid Request </h1> </body></html>"
        return HttpResponse(response_html)



def sendEmail(name, email, message):
    """
        Sends an email to antonio's gmail account to get the message ... this will be replaced later on with
        a back-end database
    """

    SERVER  = "smtp.gmail.com:587"
    FROM    = email
    TO      = ["arandaeggermont@gmail.com"]
    SUBJECT = "Contact Request"
    TEXT    = message

    usr = "arandaeggermont"
    psw = "limabean"

    subject  = "Contact Request Received"
    senddate = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

    m   = "Date: %s\r\n From: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % ( senddate , FROM, TO, subject)
    msg = "Name: %s \n email: %s \n\n %s " % (name, email, message)

    # Send the actual email
    server = smtplib.SMTP(SERVER)
    server.starttls()
    server.login(usr,psw)
    server.sendmail(FROM, TO, m+msg)
    server.quit()
