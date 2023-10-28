from django.shortcuts import render
from .models import Album, Song
from django.contrib.auth.views import LoginView

# Create your views here.
def home(request):
    return render(request, 'bandapp/home.html')

def albums(request):
    albums = Album.objects.all()
    return render(request, 'bandapp/albums.html', {'albums': albums})

def songs(request):
    songs = Song.objects.all()
    return render(request, 'bandapp/songs.html', {'songs': songs})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'