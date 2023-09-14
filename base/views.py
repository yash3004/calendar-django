from django.shortcuts import render

from json import dumps


# Create your views here.
def welcome(request):
   
    context = {
        

    }
    return render(request ,'index2.html' , context)
def about(request):
    context = {

    }
    return render(request , 'about.html' , context)
        
       


