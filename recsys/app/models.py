from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime

# Create your models here.

# class User(AbstractUser):
#     cluster = models.ForeignKey('UserCluster', on_delete=models.SET_NULL, blank=True, null=True)
#     answers = models.ManyToManyField('Answer')
#     saved_movies = models.ManyToManyField('Movie')
#     saved_events = models.ManyToManyField('Event')
#     identifier = models.CharField(max_length=40, unique=True)

#     def __str__(self):
#         return self.identifier

#     def get_answers(self):
#         return "\n".join([answer for answer in self.answers.all()])
    
#     def get_movies(self):
#         return "\n".join([movie.text for movie in self.saved_movies.all()])
    
#     def get_events(self):
#         return "\n".join([event.text for event in self.saved_events.all()])

class OLifer(models.Model):
    identifier = models.CharField(max_length=40, unique=True)
    cluster = models.ForeignKey('UserCluster', on_delete=models.SET_NULL, blank=True, null=True)
    saved_movies = models.ManyToManyField('Movie')
    saved_events = models.ManyToManyField('Event')
    answers = models.ManyToManyField('Answer', null=True, blank=True)

    def __str__(self):
        return self.identifier

    def get_answers(self):
        return "\n".join([answer for answer in self.answers.all()])
    
    def get_movies(self):
        return "\n".join([movie.text for movie in self.saved_movies.all()])
    
    def get_events(self):
        return "\n".join([event.text for event in self.saved_events.all()])

class UserCluster(models.Model):
    index = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.index)

class Question(models.Model):
    text = models.CharField(max_length=200, unique=True)
    tags = models.ManyToManyField('Tag')

    def get_tags(self):
        return "\n".join([tag.tag_name for tag in self.tag.all()])

class Answer(models.Model):
    ANSWER_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )
    belongs_to = models.ForeignKey('OLifer', on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.IntegerField(choices=ANSWER_CHOICES, default=0)

    def get_tags(self):
        return "\n".join([tag.tag_name for tag in self.tag.all()])
    
    def __str__(self):
        return '%s %s' % (self.answer, self.question.text)

class Tag(models.Model):
    tag_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return '%s' % (self.tag_name)

class Movie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(default=2019)
    genre = models.ManyToManyField('Genre')
    synopsis = models.TextField(null=True, blank=True)
    recommendation_index = models.DecimalField(max_digits=4, default=0, decimal_places=3)
    showing_until = models.DateField(default=datetime.date.today)


    def __str__(self):
        return '%s' % (self.title)

class Event(models.Model):
    # user_account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    recommendation_index = models.DecimalField(max_digits=4, default=0, decimal_places=3)
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return '%s' % (self.title)

class Genre(models.Model):
    genre_name = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.genre_name)
