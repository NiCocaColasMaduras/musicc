from django.db import models

# жанр музыки
class Genre(models.Model):
    name_en = models.CharField(max_length= 500, unique=True)
    name_ru = models.CharField(max_length= 500, unique=True)
    description = models.TextField()

    # функция для преобразования в строку
    def __str__(self):
        return self.name_ru
    
class Track(models.Model):
    title = models.CharField(max_length=500, unique=True)
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre)

    # функция для преобразования в строку
    def __str__(self):
        return self.title
