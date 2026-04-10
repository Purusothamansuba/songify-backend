import time
from mutagen.mp3 import MP3

from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Song, Playlist, PlaylistSong, Like, History
from .serializers import (
    SongSerializer, SongListSerializer, SongUploadSerializer,
    PlaylistSerializer, PlaylistSongSerializer,
    LikeSerializer, HistorySerializer
)
from .supabase_client import supabase
import re

def clean_filename(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9._-]', '_', name)  # keep safe chars only
    return name

# =========================
# 🎵 SONG VIEWSET
# =========================
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Song.objects.only(
            'id',
            'title',
            'artist',
            'album',
            'duration',
            'file_url',
            'cover_image',
            'created_at'
        ).order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return SongListSerializer
        if self.action == 'create':
            return SongUploadSerializer
        return SongSerializer

    def create(self, request, *args, **kwargs):
        serializer = SongUploadSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        file = serializer.validated_data.pop('file')

        # ✅ Title: user override OR filename
        title = request.data.get("title") or file.name.rsplit('.', 1)[0]

        # ✅ Extract duration
        try:
            audio = MP3(file)
            duration = int(audio.info.length)
        except Exception:
            return Response({"error": "Invalid MP3 file"}, status=400)

        # ⚠️ Reset file pointer after reading
        file.seek(0)

        safe_name = clean_filename(file.name)
        file_name = f"{int(time.time())}_{safe_name}"

        try:
            # Upload to Supabase
            supabase.storage.from_("songs").upload(
                file_name,
                file.read()
            )

            # Get public URL
            public_url = supabase.storage.from_("songs").get_public_url(file_name)

            if isinstance(public_url, dict):
                public_url = public_url.get("publicUrl")

        except Exception as e:
            return Response({"error": str(e)}, status=500)

        # Save to DB
        song = serializer.save(
            file_url=public_url,
            title=title,
            duration=duration
        )

        return Response(SongSerializer(song).data, status=201)


# =========================
# 📁 PLAYLIST
# =========================
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.select_related('user').only(
            'id', 'name', 'user', 'created_at'
        )


# =========================
# 🔗 PLAYLIST SONG
# =========================
class PlaylistSongViewSet(viewsets.ModelViewSet):
    queryset = PlaylistSong.objects.all()
    serializer_class = PlaylistSongSerializer

    def get_queryset(self):
        return PlaylistSong.objects.select_related('playlist', 'song')


# =========================
# ❤️ LIKE
# =========================
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.select_related('user', 'song')


# =========================
# 📜 HISTORY
# =========================
class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def get_queryset(self):
        return History.objects.select_related('user', 'song')