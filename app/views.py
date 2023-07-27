from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def my_string(request):
    return HttpResponse('<marquee><h1>This is a horizontally scrolling heading</h1></marquee>')

def my_string2(request):
    return HttpResponse('<marquee><i>This is itallic scrolling text</i></marquee>')