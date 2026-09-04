from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello I am Home page")

def about(request):
    return HttpResponse("Hello I am about page")

def shareId(request, id, name):
    return HttpResponse(f"My id of myapp is {id}")