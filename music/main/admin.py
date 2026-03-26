from django.contrib import admin
from .models import Genre, Track, Artist

#1234567890
# Register your models here.
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(Artist)
