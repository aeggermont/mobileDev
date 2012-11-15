# Create your views here.
# https://docs.djangoproject.com/en/1.4/ref/contrib/csrf/

from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template.loader import get_template
from datetime import date
from django import forms

todaydate = date.today()

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class SourceFile(forms.Form):

    source_videos = ["video one" , "video two", "video three"]

    source_files = forms.ChoiceField(choices=[(source_videos[x], source_videos[x]) for x in range(0, 3)])


class GeneralInfo(forms.Form):

    name = forms.CharField( required=False )
    short_title = forms.CharField( required=False )
    description = forms.CharField( required=False )
    start_date = forms.CharField( required=False )
    expiredate = forms.CharField( required=False )
    video_credit = forms.CharField( required=False ) 
    video_network = forms.CharField( required=False )
    content_provider = forms.CharField( required=False )
    video_category = forms.CharField( required=False )
    season_number = forms.CharField( required=False )
    episode_number = forms.CharField( required=False )
    dw_tag = forms.CharField( required=False )
    copy_edited = forms.CharField( required=False )
    regios = forms.CharField( required=False )
    embedded_video = forms.CharField( required=False )
    embedcode = forms.CharField( required=False )


def home(request):

    c = {}
    c.update(csrf(request))

    if request.method == 'POST':
        response_html = u"<html><body>>h1> Form submitted </h1></body></html>"
    
    else:
        forma = ContactForm() # An unbound form
        formb = GeneralInfo()
        formc = SourceFile()

        return render_to_response("videorobot/index.html", {
            "formc":formc,
            "forma":forma, 
            "formb":formb, 
        },)

