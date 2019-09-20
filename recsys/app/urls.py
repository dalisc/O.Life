from django.urls import path
from . import views

urlpatterns = [
path('', views.homepage, name='homepage'),
path('events/', views.events, name='events'),
path('events/add', views.add_event, name='add_event'),
path('movies/', views.movies, name='movies'),
path('movies/add', views.add_movie, name='add_movie'),
path('polls/', views.polls, name='polls'),

]