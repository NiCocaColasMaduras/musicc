from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Genre, Track, Artist
from .forms import GenreForm, TrackForm, ArtistForm

# главная
def index(request):
    return render(request, 'index.html')

#==============================
#   ЖАНРЫ
#==============================

# список жанров
def genres(request):
    # получем список жанров
    genres = Genre.objects.all()
    
    return render(request, 'genres.html', {'genres': genres})

# добавить жанр
def add_genre(request):
    # получили данные, нужно сохранить жанр в базу
    if request.method == "POST":
        # получаем данные из формы
        genre = GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    # это простой запрос, нужно показать форму
    else:
        genreform = GenreForm()
        return render(request, 'add_genre.html', {'form': genreform})
    
# изменить жанр
def edit_genre(request, id_genre):
    # получим жанр, который нужно редактировать
    g = Genre.objects.get(id=id_genre)

    # получили данные, нужно сохранить жанр в базу
    if request.method == "POST":
        # получаем данные из формы
        genre = GenreForm(request.POST, instance=g)
        if genre.is_valid():
            genre.save()
            return redirect('/genres')

    # это простой запрос, нужно показать форму
    else:
        genreform = GenreForm(instance=g)
        return render(request, "add_genre.html", {"form": genreform})
    
# удаление жанра
def delete_genre(request, id_genre):
    # получим жанр из базы данных
    genre = Genre.objects.get(id=id_genre)
    # удалим жанр
    genre.delete()
    # покажем сообщение
    return HttpResponse('<h1>Жанр успешно удалён</h1><br><a href="/genres" class="EmptyForm">На главную</a>')


#==============================
#   ТРЕКИ
#==============================

# список треков
def tracks(request):
    # получем список треков
    tracks = Track.objects.all()

    # получем список жанров
    genres = Genre.objects.all()

    # получем список исполнителей из базы
    a = Artist.objects.all()
    artist = None
    # Передали исполнителя

    if request.method == "POST":
        id_artist = request.POST.get('artist')
        artist = Artist.objects.get(id=id_artist)
        tracks = Track.objects.filter(artist=artist)
    return render(request, 'tracks.html', {'genres': genres, 'tracks': tracks, 'artists': a, 'current_artists': artist})

# добавить трек
def add_track(request):
    # получили данные, нужно сохранить жанр в базу
    if request.method == "POST":
        # получаем данные из формы
        track = TrackForm(request.POST)

        if track.is_valid():
            track.save()
        return redirect('/tracks')
    # это простой запрос, нужно показать форму
    else:
        trackform = TrackForm()
        return render(request, 'add_track.html', {'form': trackform})
    
# изменить трек
def edit_track(request, id_track):
    # получим жанр, который нужно редактировать
    t = Track.objects.get(id=id_track)

    # получили данные, нужно сохранить жанр в базу
    if request.method == "POST":
        # получаем данные из формы
        track = TrackForm(request.POST, instance=t)

        if track.is_valid():
            track.save()
            return redirect('/tracks')

    # это простой запрос, нужно показать форму
    else:
        trackform = TrackForm(instance=t)
        return render(request, "add_track.html", {"form": trackform})
    
# удаление трека
def delete_track(request, id_track):
    # получим жанр из базы данных
    track = Track.objects.get(id=id_track)

    # удалим жанр
    track.delete()

    # покажем сообщение
    return HttpResponse('<h1>Трек успешно удалён</h1><br><a href="/tracks" class="EmptyForm">На главную</a>')


#==============================
#   АРТИСТЫ
#==============================

# список артистов
def artists(request):
    # получем список исполнителей из базы
    artist = Artist.objects.all()

    # получем список треков
    tracks = Track.objects.all()

    return render(request, 'artists.html', {'artists': artist, 'tracks': tracks})

# добавить артиста
def add_artist(request):
    # получили данные, нужно сохранить артиста в базу
    if request.method == "POST":
        # получаем данные из формы
        artist = ArtistForm(request.POST)

        if artist.is_valid():
            artist.save()
        return redirect('/artists')
    # это простой запрос, нужно показать форму
    else:
        ArtistForm = ArtistForm()
        return render(request, 'add_artist.html', {'form': ArtistForm})
    
# изменить артиста
def edit_artist(request, id_artist):
    # получим исполнителя, которого нужно редактировать
    a = Artist.objects.get(id=id_artist)

    # получили данные, нужно сохранить исполнителя в базу
    if request.method == "POST":
        # получаем данные из формы
        artist = ArtistForm(request.POST, instance=a)
        if artist.is_valid():
            artist.save()
            return redirect('/artists')

    # это простой запрос, нужно показать форму
    else:
        ArtistForm = ArtistForm(instance=a)
        return render(request, "add_artist.html", {"form": ArtistForm})
    
# удаление артиста
def delete_artist(request, id_artist):
    # получим исполнителя из базы данных
    artist = Artist.objects.get(id=id_artist)

    # удалим исполнителя
    artist.delete()

    # покажем сообщение
    return HttpResponse('<h1>Исполнитель успешно удалён</h1><br><a href="/artists" class="EmptyForm">На главную</a>')