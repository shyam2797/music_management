from django import forms
from django.contrib.auth.models import User

from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_title']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['album','song_title', 'audio_file']