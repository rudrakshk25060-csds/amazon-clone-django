from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello I am Home page of myapp1")

def about(request):
    return HttpResponse("Hello I am about page myapp1")

def shareid(request, id, name):
    return HttpResponse(f"My id of myapp1 is {id} and my name is {name}")

def year(request, year):
    return HttpResponse(f"The year of myapp1 is {year}")


def key_word_args(request ,**kwargs):
    return HttpResponse(f"<h1>your name is {kwargs["name"]} and your id is {kwargs["id"]}</h1>")