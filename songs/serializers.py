from rest_framework import serializers
from .models import Song, Playlist, PlaylistSong, Like, History


# ✅ Existing serializers (unchanged)

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
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


# ✅ NEW: Upload serializer

class SongUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)

    class Meta:
        model = Song
        fields = [
            'id',
            'title',
            'artist',
            'album',
            'duration',
            'cover_image',
            'file_url',
            'file'
        ]
        read_only_fields = ['file_url']

    # Optional validation
    def validate_file(self, file):
        if not file.name.endswith('.mp3'):
            raise serializers.ValidationError("Only MP3 files allowed")
        if file.size > 50 * 1024 * 1024:
            raise serializers.ValidationError("Max size 50MB")
        return file