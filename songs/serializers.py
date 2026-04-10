from rest_framework import serializers
from .models import Song, Playlist, PlaylistSong, Like, History

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # FIX: Added file_url, duration, and cover_image so the player has what it needs
        fields = ['id', 'title', 'artist', 'file_url', 'duration', 'cover_image']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistSong
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'