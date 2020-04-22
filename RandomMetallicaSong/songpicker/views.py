from django.shortcuts import render
from django.http import HttpResponse
from .models import Song
from random import randint


def index(request):
    return render(request, 'songpicker/index.html')


# Takes a random song from list of all songs and
# shows it as a youtube frame on page
def pick(request):
    songs = Song.objects.all()
    random_index = randint(0, len(songs)-1)
    s = songs[random_index]
    embed_link = s.embed_link()
    return render(request, 'songpicker/pick.html', context={'song': s, 'embed': embed_link})
