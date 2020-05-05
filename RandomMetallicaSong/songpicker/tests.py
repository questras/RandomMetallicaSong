from django.test import TestCase
from django.shortcuts import reverse
from html import unescape
import time

from .database_with_songs_setup import setup_database_with_songs
from .models import Song


class IndexViewTests(TestCase):
    def test_can_access_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class PickViewTests(TestCase):
    def test_view_redirects(self):
        setup_database_with_songs()
        response = self.client.get(reverse('pick'))
        self.assertEqual(response.status_code, 302)


class SongViewTests(TestCase):
    def test_view_for_every_song(self):
        """
        Test if song_view can be accessed for each song in database.
        Each request to song_view sends a request to youtube page, so
        test for each song is made every 1 second.
        Approximate time of test: 3 min.
        """
        setup_database_with_songs()
        songs = Song.objects.all()

        print("\nRunning song_view test for every song.")
        print("This may take a while (approx. 5min).")
        for song in songs:
            url = reverse('song_view', kwargs={'song_id': song.pk})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            time.sleep(1)


class SongListViewTests(TestCase):
    def test_can_access_view(self):
        response = self.client.get(reverse('song_list_view'))
        self.assertEqual(response.status_code, 200)

    def test_every_song_is_seen(self):
        """
        Test if every song from database is seen in table in view.
        """
        setup_database_with_songs()
        songs = Song.objects.all()
        response = self.client.get(reverse('song_list_view'))
        unescaped_response = unescape(response.content.decode())

        for song in songs:
            self.assertIn(song.name, unescaped_response)
            self.assertIn(song.album, unescaped_response)
