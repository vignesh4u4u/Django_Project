from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def home(request):
    return  HttpResponse("hello , how are you django")

# Create your views here.
