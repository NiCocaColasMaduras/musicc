from django.db import models

# жанр музыки
class Genre(models.Model):
    name_en = models.CharField(max_length= 500, unique=True)
    name_ru = models.CharField(max_length= 500, unique=True)
    description = models.TextField()

    # функция для преобразования в строку
    def __str__(self):
        return self.name_ru

# Исполнитель (группа или человек)
class Artist(models.Model):
    name = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='artists/', null=True)

    def __str__(self):
        return self.name
    
class Track(models.Model):
    title = models.CharField(max_length=500, unique=True)
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, null=True)
    audio_file = models.FileField(upload_to='music/tracks/', blank=True, null=True)

    # функция для преобразования в строку
    def __str__(self):
        return self.title
