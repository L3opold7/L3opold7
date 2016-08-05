from django.conf.urls import url

from common.views import *

urlpatterns = [
    url(r'^$', home, name='index'),

    # 가입
    url(r'^create/$', CreateUser.as_view(), name='create'),

    # 유저정보 보기
    url(r'^user/(?P<slug>[\w-]+)/$', ViewUser.as_view(), name='view_user'),

    # 유저 삭제하기
    url(r'^user/(?P<slug>[\w-]+)/delete/$', DeleteUser.as_view(), name='delete_user'),
]
