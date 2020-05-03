from django.shortcuts import render, redirect, reverse
import random
import requests
import bs4

from .models import Song


def get_youtube_embed_link(name, album):
    search_query = f'metallica+{name}+{album}'.replace(' ', '+')
    search_url = f'https://www.youtube.com/results?search_query={search_query}'

    response = requests.get(search_url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    elements = soup.find_all('a')

    video_id = ''
    for element in elements:
        if 'href' in element.attrs and 'watch' in element['href']:
            video_id = element['href'].split('=')[1]
            break

    return f'https://www.youtube.com/embed/{video_id}'


def index(request):
    return render(request, 'songpicker/index.html')


def song_view(request, song_id):
    """
    Song view with embedded youtube video.
    """
    song = Song.objects.get(pk=song_id)
    embed_url = get_youtube_embed_link(song.name, song.album)
    context = {
        'song': song,
        'embed_url': embed_url,
    }
    return render(request, 'songpicker/song.html', context=context)


def pick(request):
    """
    Redirect to song_view of random song.
    """
    songs = Song.objects.all()
    random_song = random.choice(songs)

    return redirect(reverse('song_view', kwargs={'song_id': random_song.pk}))
