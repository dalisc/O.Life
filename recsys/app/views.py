from django.shortcuts import render
from django.http import HttpResponse
from app.models import Event, Movie

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def events(request):

    # events = Event.objects.filter(user_account=request.user).order_by('-recommendation_index')
    events = Event.objects.all().order_by('-recommendation_index')

    context = {
        'event_list': events,
    }

    return render(request, 'events.html', context=context)

def movies(request):

    # movies = Movie.objects.filter(user_account=request.user).order_by('-recommendation_index')
    movie = Movie.objects.all().order_by('-recommendation_index')

    context = {
        'movie_list': movies,
    }

    return render(request, 'movies.html', context=context)