from django.contrib import admin
from .models import Song, Playlist, PlaylistSong, Like, History

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(PlaylistSong)
admin.site.register(Like)
admin.site.register(History)