from rest_framework import serializers
from .models import Song, Playlist, PlaylistSong, Like, History

ALLOWED_EXTENSIONS = {
    '.mp3', '.wav', '.flac', '.ogg',
    '.m4a', '.aac', '.opus'
}
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
    def validate_file(self, value):
        ext = '.' + value.name.lower().rsplit('.', 1)[-1]

        if ext not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError(
                f"Unsupported format: {ext}"
            )

        return value