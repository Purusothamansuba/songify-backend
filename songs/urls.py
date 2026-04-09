from rest_framework.routers import DefaultRouter
from .views import (
    SongViewSet, PlaylistViewSet,
    PlaylistSongViewSet, LikeViewSet, HistoryViewSet
)

router = DefaultRouter()

router.register(r'songs', SongViewSet, basename='song')
router.register(r'playlists', PlaylistViewSet, basename='playlist')
router.register(r'playlist-songs', PlaylistSongViewSet, basename='playlist-song')
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'history', HistoryViewSet, basename='history')

urlpatterns = router.urls