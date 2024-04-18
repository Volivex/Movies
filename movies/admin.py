from django.contrib import admin
from movies.models import *

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )

@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'role',
    )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'rating',
        'id',
    )

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'movie',
        'likes',
    )