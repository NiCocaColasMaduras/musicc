from django import forms
from .models import Genre, Track
 
#class GenreForm(forms.Form):
    #name_ru = forms.CharField(label='Название на русском')
    #name_en = forms.CharField(label='Название на английском')
    #description = forms.CharField(label='Описание', widget=forms.Textarea)

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        labels = {
            'name_ru': 'Название на русском',
            'name_en': 'Название на английском',
            'description': 'Описание',
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
        labels = {
            'title': 'Название',
            'duration': 'Длительность',
            'genres': 'Жанры',
        }