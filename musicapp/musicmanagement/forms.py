from django import forms
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
