"""
Module to scrape wikipedia page with all metallica songs
and get list of songs and corresponding albums.
"""

import pandas as pd

def get_songs_list():
    """
    Scrape wikipedia page with all Metallica songs and
    return list of all songs and corresponding albums.
    :return: List of (song, album) tuples.
    """
    url = 'https://en.wikipedia.org/wiki/List_of_songs_recorded_by_Metallica'
    songs = pd.read_html(url)[-2]

    songs['Title'] = songs['Title'].apply(lambda x: x.split('"')[1])
    songs = songs[['Title', 'Release']]
    songs_list = list(songs.itertuples(index=False, name=None))

    return songs_list