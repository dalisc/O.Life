from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Event, Movie
import random
        
class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('identifier',)

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('identifier', 'answers', 'saved_movies', 'saved_events')

class EventCreationForm(forms.ModelForm):

    class Meta(UserCreationForm):
        model = Event
        exclude = ('recommendation_index',)

    def form_valid(self, form):
        event_model = form.save(commit=False)
        # event_model.recommendation_index = random.uniform(0, 1)
        event.save()

class MovieCreationForm(forms.ModelForm):

    class Meta(UserCreationForm):
        model = Movie
        exclude = ('recommendation_index',)

    def form_valid(self, form):
        movie_model = form.save(commit=False)
        # movie_model.recommendation_index = random.uniform(0, 1)
        movie.save()

        