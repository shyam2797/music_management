from django.shortcuts import render
from .forms import SongForm
from .models import Song
from django.db.models import Q

def create_song(request):
    form = SongForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        song = form.save(commit=False)
        song.audio_file=request.FILES['audio_file']
        file = song.audio_file.url.split(".")[-1]
        if file != 'mp3':
            context = {'form' : form ,'error' : ' *** Enter a valid file name *** '}
            return render(request, 'musicmanagement/create_song.html',context)
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
        search =  request.GET.get('search')
        try:
            status=Song.objects.filter(Q(song_title__icontains=search)  | Q(album__icontains=search) | Q(artist__icontains=search ))
        except:
            status=None
        return render(request,"musicmanagement/search.html",{"songs":status})
    else:
        return render(request,"musicmanagement/search.html",{})