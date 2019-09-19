from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def events(request):
    return render(request, 'events.html')

def movies(request):
    return render(request, 'movies.html')