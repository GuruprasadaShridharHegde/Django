from django.shortcuts import render
# below are my lines
from django.http import HttpResponse
# Create your views here.
def home(requests): # this is a route
    return HttpResponse("Hey I am a Django Server")

 