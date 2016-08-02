from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # 가입
    url(r'^create/$', views.CreateUser.as_view(), name='create'),

    # 유저정보 보기
    url(r'^user/(?P<slug>[\w-]+)/$', views.ViewUser.as_view(), name='view_user'),

    # 유저 삭제하기
    url(r'^user/(?P<slug>[\w-]+)/delete/$', views.DeleteUser.as_view(), name='delete_user'),
]
