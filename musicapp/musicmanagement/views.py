from django.shortcuts import render
from .forms import AlbumForm , SongForm , ArtistForm
from .models import Song

def create_album(request):
    form = AlbumForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        album=form.save(commit=False)
        album.save()
        songs=Song.objects.all()
        return render(request,'musicmanagement/index.html',{'songs' : songs})

    context={"form" : form }
    return render(request , 'musicmanagement/create_album.html', context)

def create_artist(request):
    form = ArtistForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        artist = form.save(commit = False)
        artist.save()
        songs=Song.objects.all()
        return render(request , 'musicmanagement/index.html',{ 'songs' : songs})

    context={"form" : form }
    return render(request , 'musicmanagement/create_artist.html',context)


def create_song(request):
    form = SongForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        song = form.save(commit=False)
        song.audio_file=request.FILES['audio_file']
        song.save()
        songs=Song.objects.all()
        return render(request ,'musicmanagement/index.html', {'songs' : songs})
    context = {'form' : form}
    return render(request ,'musicmanagement/create_song.html' , context)

def delete_song(request ,song_id):
    song = Song.objects.get(pk=song_id)
    song.delete()
    songs=Song.objects.all()
    return render( request , 'musicmanagement/index.html' ,{'songs' : songs })

def index(request):
    songs = Song.objects.all()
    return render(request, 'musicmanagement/index.html', {'songs': songs})

def search(request):
    if request.method == 'GET':
        song_name =  request.GET.get('search')
        try:
            status = Song.objects.filter(song_title__icontains=song_name)
        except:
            status = None
        return render(request,"musicmanagement/search.html",{"songs":status})
    else:
        return render(request,"musicmanagement/search.html",{})