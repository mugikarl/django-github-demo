from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django Blog!")

def about(request):
    return HttpResponse("About page")

def post_list(request):
    return HttpResponse("Post list coming soon")

def contact(request):
    return HttpResponse("Contact us")

