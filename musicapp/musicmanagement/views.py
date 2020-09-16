from django.shortcuts import render , get_object_or_404
from django.db.models import Q
from .forms import AlbumForm , SongForm
from .models import Album,Song

# Create your views here.
def create_album(request):
    form = AlbumForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        album=form.save(commit=False)
        album.save()
        return render(request,musicmanagement/detail.html,{'album' : album})

    context={
        "form" : form
    }
    return render(request , musicmanagement/create_album.html, context)

def create_song(request):
    form = SongForm(request.POST or None , request.FILES or None)
    album=get_object_or_404(Album , pk=album_id)
    if form.is_valid():
        album_songs = album.song_set.all()
        for s in album_songs:
            if s.song_title == form.cleaned_data.get('song_title'):
                context = {
                    'album': album,
                    'form': form,
                    'error messege' : 'Song already exist',
                }
                return render(request, musicmanagement/create_song.html , context)
        song = form.save(commit=False)
        song.album=album
        song.audio_file=request.FILES['audio_file']

        song.save()

        return render(request ,musicmanagement/detail.html, {'album' : album})

    context = {
        'album' : album,
        'form' : form,
    }
    return render(request ,musicmanagement/create_song.html , context)

def delete_album(request , album_id):
    album = get_object_or_404(Album , pk = album_id)
    album.delete()
    albums = Album.objectes.all()
    return render(request , musicmanagement/index.html , {'albums':albums})

def delete_song(request ,album_id ,  song_id):
    album = get_object_or_404(Album , pk = album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render( request , musicmanagement/detail.html ,{'album' : album})
def detail(request , album_id):
    album = get_object_or_404(Album , pk = album_id)
    return render(request , musicmanagement/detail.html , {'album' : album})

def index(request):
    albums = Album.objects.all()
    song_results = Song.objects.all()
    query = request.GET.get("q")
    if query :
        albums = albums.filter(Q(album_title__icontains=query)).distinct()
        song_results = song_results.filter(Q(song_title__icontains=query)).distinct()
        return render(request , musicmanagement/index.html,{'albums' : albums , 'songs' : song_results})
    return render(request , musicmanagement/index.html ,{'albums' : albums})









