from django.conf.urls.defaults import *
from mysite.contact.views import *

urlpatterns = patterns('mysite.contact.views',
    (r'', contact),
)
