"""
Module to add to database all scraped Metallica songs.
Run 'setup' function from manage.py shell.
"""
from .models import Song
from .songs_scraper import get_songs_list


def setup():
    """
    Add all Metallica songs from [get_songs_list] to database.
    :return:
    """
    songs_list = get_songs_list()
    for idx, (name, album) in enumerate(songs_list):
        obj = Song(name=name, album=album)
        obj.save()
