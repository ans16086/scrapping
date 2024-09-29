from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'scraping'
urlpatterns = [


#path('',TemplateView.as_view(template_name = "userprof.html")),
#path('userp/',userprofo) ,
#path('get_subscriber_count/',get_subscriber_count,name='get_subscribers_count') 
path('data_p/',person_data.as_view())


  ]