from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    artist = models.CharField(max_length=200, db_index=True)
    album = models.CharField(max_length=200, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    file_url = models.URLField()
    cover_image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']  # default ordering

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name


class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['playlist', 'song']),
        ]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'song']  # prevent duplicate likes
        indexes = [
            models.Index(fields=['user', 'song']),
        ]


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    played_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'played_at']),
        ]