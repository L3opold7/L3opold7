from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# 장고 인증 뷰
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 어드민
    url(r'^admin/', admin.site.urls),

    # 장고 인증 로그인 기본 뷰 login.html로 바꿈
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}),

    # 장고 인증 로그아웃 / 로 리다이렉트 시키기
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),

    # 장고 인증시스템 사용 (core.urls 에 세부사항 기술)
    url('^', include('django.contrib.auth.urls')),

    # 글
    url(r'^post/', include('blog.urls')),
    url(r'^', include('common.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

