from django.db import models

class Album(models.Model):
    album_title = models.CharField(max_length=50)

    def __str__(self):
        return self.album_title

class Artist(models.Model):
    artist_name = models.CharField(max_length=50)

    def __str__(self):
        return self.artist_name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist= models.ForeignKey(Artist,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=50)
    audio_file = models.FileField(default='')

    def __str__(self):
        return self.song_title
