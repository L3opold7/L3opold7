from django.conf.urls import url

from . import views

urlpatterns = [
    # 글리스트
    url(r'^$', views.ListPost.as_view(), name='list_post'),

    # 태그로 검색하기
    url(r'^tag/(?P<slug>[\w-]+)/$', views.TagListPost.as_view(), name='tag_list_post'),

    # 글 새로 쓰기
    url(r'^new/$', views.NewPost.as_view(), name='new_post'),

    # 글 보기
    url(r'^(?P<pk>[0-9]+)/$', views.ViewPost.as_view(), name='view_post'),

    # 글 투표 ajax에 사용됨
    url(r'^(?P<id>[0-9]+)/vote/$', views.vote_post, name='vote_post'),

    # 글 삭제 역시 ajax에서 사용됨
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeletePost.as_view(), name='delete_post'),

    # 글 수정
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdatePost.as_view(), name='update_post'),

    # 사진 업로드
    url(r'^(?P<pk>[0-9]+)/upload_photo/$', views.upload_photo, name='upload_photo'),
]
