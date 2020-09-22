
from django.conf.urls import url
from . import views

app_name = 'musicmanagement'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^create_artist/$', views.create_artist, name='create_artist'),
    url(r'^create_song/$', views.create_song, name='create_song'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<song_id>[0-9]+)/delete_song/$', views.delete_song, name='delete_song'),
]