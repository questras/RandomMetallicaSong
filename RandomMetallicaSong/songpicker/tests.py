from django.test import TestCase
from django.shortcuts import reverse
from .database_with_songs_setup import setup_database_with_songs
import time

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
        :return:
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
