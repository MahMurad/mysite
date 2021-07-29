from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Homepage(request):
    return HttpResponse('<h1>Welcome to RUET Buy<h1>')
