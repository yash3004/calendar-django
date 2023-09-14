from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.welcome, name= "welcome"),
    path('about/' , views.about , name = "about"),
 
]