from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    return HttpResponse ("Helle vignesh, how are you?")

def detail(request):
    return HttpResponse ("this for more url and view purpose")

def dynamic_url(request,post_id):
    return HttpResponse(f"you are view post url page ID is {post_id}")
