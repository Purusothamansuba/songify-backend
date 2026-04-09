from rest_framework.routers import DefaultRouter
from .views import (
    SongViewSet, PlaylistViewSet,
    PlaylistSongViewSet, LikeViewSet, HistoryViewSet
)

router = DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'playlist-songs', PlaylistSongViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = router.urls