from django.db import models


class Song(models.Model):
    song_name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    youtube_link = models.CharField(max_length=200)

    def __str__(self):
        return self.song_name

    def embed_link(self):
        embed_link = 'https://www.youtube.com/embed/' + self.youtube_link[32:]
        return embed_link
