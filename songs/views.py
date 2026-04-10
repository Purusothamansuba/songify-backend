import time
import re
from mutagen import File

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


# =========================
# 🔒 SAFE FILENAME
# =========================
def clean_filename(name):
    name = name.lower()
    return re.sub(r'[^a-z0-9._-]', '_', name)


# =========================
# 🎵 ALLOWED AUDIO FORMATS
# =========================
ALLOWED_EXTENSIONS = {
    '.mp3', '.wav', '.flac', '.ogg',
    '.m4a', '.aac', '.opus'
}


# =========================
# 🎵 SONG VIEWSET
# =========================
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Song.objects.only(
            'id', 'title', 'artist', 'album',
            'duration', 'file_url',
            'cover_image', 'created_at'
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

        # =========================
        # 📁 VALIDATE EXTENSION
        # =========================
        ext = '.' + file.name.lower().rsplit('.', 1)[-1]
        if ext not in ALLOWED_EXTENSIONS:
            return Response(
                {"error": f"Unsupported file format: {ext}"},
                status=400
            )

        # =========================
        # 📝 TITLE
        # =========================
        title = request.data.get("title") or file.name.rsplit('.', 1)[0]

        # =========================
        # ⏱️ EXTRACT DURATION (ALL FORMATS)
        # =========================
        try:
            audio = File(file)

            if audio is None:
                return Response(
                    {"error": "Unsupported or corrupted audio file"},
                    status=400
                )

            if not hasattr(audio, "info") or not hasattr(audio.info, "length"):
                return Response(
                    {"error": "Cannot read audio metadata"},
                    status=400
                )

            duration = int(audio.info.length)

        except Exception as e:
            return Response(
                {"error": f"Audio processing failed: {str(e)}"},
                status=400
            )

        # ⚠️ Reset file pointer
        file.seek(0)

        # =========================
        # 📦 SAFE FILE NAME
        # =========================
        safe_name = clean_filename(file.name)
        file_name = f"{int(time.time())}_{safe_name}"

        # =========================
        # ☁️ UPLOAD TO SUPABASE
        # =========================
        try:
            supabase.storage.from_("songs").upload(
                file_name,
                file.read()
            )

            public_url = supabase.storage.from_("songs").get_public_url(file_name)

            if isinstance(public_url, dict):
                public_url = public_url.get("publicUrl")

        except Exception as e:
            return Response(
                {"error": f"Upload failed: {str(e)}"},
                status=500
            )

        # =========================
        # 💾 SAVE TO DATABASE
        # =========================
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