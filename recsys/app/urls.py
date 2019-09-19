from django.urls import path
from . import views

urlpatterns = [
path('', views.homepage, name='homepage'),
path('events/', views.events, name='events'),
path('movies/', views.movies, name='movies'),
path('polls/', views.polls, name='polls'),
]