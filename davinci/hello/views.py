from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Da Vinci")

def greeting(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")