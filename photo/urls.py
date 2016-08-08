from django.conf.urls import url
from photo.views import *


urlpatterns = [
    # /photo/
    url(r'^$', AlbumLV.as_view(), name='index'),

    # /photo/album/
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),

    # /photo/album/1
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),

    # photo/photo/1
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),
]
