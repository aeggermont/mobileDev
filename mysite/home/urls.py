from django.conf.urls.defaults import *
from mysite.home.views import *

urlpatterns = patterns('mysite.home.views',
    (r'', home),
)
