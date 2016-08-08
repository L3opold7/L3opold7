"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from Leopold.views import HomeView

urlpatterns = [
    # Admin 페이지
    url(r'^admin/', include(admin.site.urls)),

    # index 페이지
    url(r'^$', HomeView.as_view(), name='home'),

    # bookmark 앱
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),

    # blog 앱
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # photo 앱
    url(r'^photo/', include('photo.urls', namespace='photo')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
