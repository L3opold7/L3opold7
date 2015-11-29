from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post


def post_list(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
