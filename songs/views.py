from rest_framework import viewsets
from .models import Song, Playlist, PlaylistSong, Like, History
from .serializers import (
    SongSerializer, SongListSerializer,
    PlaylistSerializer, PlaylistSongSerializer,
    LikeSerializer, HistorySerializer
)


class SongViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Song.objects.only(
            'id', 'title', 'artist', 'album', 'duration'
        ).order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return SongListSerializer
        return SongSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.select_related('user')


class PlaylistSongViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSongSerializer

    def get_queryset(self):
        return PlaylistSong.objects.select_related('playlist', 'song')


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.select_related('user', 'song')


class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer

    def get_queryset(self):
        return History.objects.select_related('user', 'song')