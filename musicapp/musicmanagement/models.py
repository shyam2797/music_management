from django.db import models


class Album(models.Model):
    album_title = models.CharField(max_length=500)

    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')

    def __str__(self):
        return self.song_title
