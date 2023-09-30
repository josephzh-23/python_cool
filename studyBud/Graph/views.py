from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getStudent(request, id):
    return HttpResponse("ee")

def printProfile(request):
    print(request)
    return HttpResponse("ee")