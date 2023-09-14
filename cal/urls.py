from django.urls import re_path , include
from . import views


app_name = 'cal'
urlpatterns = [
    
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
	re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    re_path(r'^booking/$' , views.booking, name= 'bookings'),
    re_path(r'^teacher/$' , views.teacher , name = 'teacher')
]
