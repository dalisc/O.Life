from django.shortcuts import render
from django.http import HttpResponse
from app.models import Event, Movie
from django.utils import timezone

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

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