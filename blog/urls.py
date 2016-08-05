from django.conf.urls import url

from blog.views import *

urlpatterns = [
    # 글리스트
    url(r'^$', PostLV.as_view(), name='index'),

    # 글 새로 쓰기
    url(r'^new/$', NewPost.as_view(), name='new_post'),

    # 글 보기
    url(r'^(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # 글 투표 ajax에 사용됨
    url(r'^(?P<slug>[-\w]+)/vote/$', vote_post, name='vote_post'),

    # 글 삭제 역시 ajax에서 사용됨
    url(r'^(?P<slug>[-\w]+)/delete/$', DeletePost.as_view(), name='delete_post'),

    # 글 수정
    url(r'^(?P<slug>[-\w]+)/update/$', UpdatePost.as_view(), name='update_post'),

    # 사진 업로드
    url(r'^(?P<slug>[-\w]+)/upload_photo/$', upload_photo, name='upload_photo'),

    # 태그 클라우드
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),

    # 글에서 태그 리스트
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
]
