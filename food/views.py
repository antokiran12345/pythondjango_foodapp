from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hi")

def item(request):
    return HttpResponse("<H1>This is an item</H1>")

