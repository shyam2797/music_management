from django import forms
from django.contrib.auth.models import User

from .models import Album, Song , Artist


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_title']

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ['artist_name']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['album','artist','song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class meta:
        model = User
        fields = ['name' , 'email' , 'password']