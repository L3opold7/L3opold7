from django.shortcuts import render
from django.utils import timezone

from blog.models import Post


def post_list(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'post_list.html', {'posts': posts})