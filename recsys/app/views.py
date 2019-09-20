from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Event, Movie
from app.forms import EventCreationForm, MovieCreationForm
from django.utils import timezone
from app import apis
from django.core import serializers
from django.http.response import JsonResponse

# Create your views here.

def homepage(request):

    movie_id = apis.getMovieId("maleficent", 2014)
    movies = apis.getSimilarMovies(movie_id)

    events = Event.objects.filter(date__gte=timezone.now()).order_by('-recommendation_index')
    # eventsJson = JsonResponse(list(events.values()), safe=False)
    
    # serialized_object = serializers.serialize('json', events[0])
    index = apis.compareEvent(events[0], events[1])

    context = {
        'movie_id': movie_id,
        'movies': movies,
        'index': index,
    }

    return render(request, 'homepage.html', context=context)

def events(request):

    # events = Event.objects.filter(user_account=request.user).order_by('-recommendation_index')
    events = Event.objects.filter(date__gte=timezone.now()).order_by('-recommendation_index')

    context = {
        'event_list': events,
    }

    return render(request, 'events.html', context=context)

def movies(request):

    # movies = Movie.objects.filter(user_account=request.user).order_by('-recommendation_index')
    movies = Movie.objects.filter(showing_until__gte=timezone.now()).order_by('-recommendation_index')

    context = {
        'movie_list': movies,
    }

    return render(request, 'movies.html', context=context)

def polls(request):

    return render(request, 'polls.html')

def add_event(request):

    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.recommendation_index = 0.7
            event = event.save()
            return redirect('events')
    else:
        form = EventCreationForm()
    return render(request, 'add_event.html', {'form': form})

def add_movie(request):

    if request.method == 'POST':
        form = MovieCreationForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.recommendation_index = 0.7
            movie = movie.save()
            return redirect('movies')
    else:
        form = MovieCreationForm()
    return render(request, 'add_movie.html', {'form': form})

