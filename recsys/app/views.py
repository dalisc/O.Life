from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Event, Movie, OLifer
from app.forms import EventCreationForm, MovieCreationForm
from django.utils import timezone
from app import apis
from django.core import serializers
from django.http.response import JsonResponse

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def events(request):

    events_to_date = Event.objects.filter(date__gte=timezone.now()).order_by('-recommendation_index')
    events = Event.objects.order_by('-recommendation_index')
    saved_events = get_saved_events(request)

    context = {
        'event_list': events,
        'saved_events': saved_events,
    }

    return render(request, 'events.html', context=context)

def movies(request):

    movies_to_date = Movie.objects.filter(showing_until__gte=timezone.now()).order_by('-recommendation_index')
    movies = Movie.objects.order_by('-recommendation_index')
    saved_movies = get_saved_movies(request)
    
    context = {
        'movie_list': movies,
        'saved_movies': saved_movies,
    }

    return render(request, 'movies.html', context=context)

def polls(request):

    return render(request, 'polls.html')

def add_event(request):

    saved_events = get_saved_events(request)

    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            index = apis.compareToSavedEvents(event.title, event.description, get_saved_events(request))
            event.recommendation_index = index
            event = event.save()
            return redirect('events')
    else:
        form = EventCreationForm()
        
    context = {
        'saved_events': saved_events,
        'form':form,
    }

    return render(request, 'add_event.html', context=context)

def add_movie(request):

    if request.method == 'POST':
        form = MovieCreationForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            index = apis.compareToSavedMovies(movie.title, movie.synopsis, get_saved_movies(request))
            movie.recommendation_index = index
            movie = movie.save()
            return redirect('movies')
    else:
        form = MovieCreationForm()
    return render(request, 'add_movie.html', {'form': form})

def get_saved_events(request):
    users_list = OLifer.objects.all()
    saved_events = []

    for users in users_list:
        saved_events_list = users.saved_events.all()
        for event in saved_events_list:
            if (event in saved_events):
                print("Event is already in list")
            else:
                saved_events.append(event)

    return saved_events

def get_saved_movies(request):
    users_list = OLifer.objects.all()
    saved_movies = []
    
    for users in users_list:
        saved_movies_list = users.saved_movies.all()
        for movie in saved_movies_list:
            if (movie in saved_movies):
                print("Movie is already in list")
            else:
                saved_movies.append(movie)

    return saved_movies


