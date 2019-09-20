from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, Question, Tag, Movie, Event, UserCluster, Genre, OLifer, Answer


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('identifier', 'password1', 'password2')}
        ),
    )
    list_display = ['identifier', 'get_movies', 'get_events',]

    def get_movies(self, obj):
        return "\n".join([movie.text for movie in obj.saved_movies.all()])
    
    def get_events(self, obj):
        return "\n".join([event.text for event in obj.saved_events.all()])

# admin.site.register(User, UserAdmin)
# admin.site.register(Question)
# admin.site.register(Tag)
admin.site.register(Movie)
admin.site.register(Event)
# admin.site.register(UserCluster)
# admin.site.register(Genre)
admin.site.register(OLifer)
# admin.site.register(Answer)
