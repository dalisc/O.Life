from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
        
class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('identifier',)

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('identifier', 'answers', 'saved_movies', 'saved_events')