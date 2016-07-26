from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.utils import timezone

from blog.models import Post, Photo
from blog.forms import PostForm, PhotoForm


def post_list(request):
    posts = Post.objects.all().order_by('modified_at').reverse()
    photos = Photo.objects.all()
    return render(request, 'post_list.html', {'posts': posts, 'photos': photos})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    photos = Photo.objects.filter(post_id=post.id)
    return render(request, 'post_detail.html', {'post': post, 'photos': photos})


def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/post/'+str(post.pk)+'/')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/post/'+str(post.pk)+'/')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        post.delete()
        return redirect('/')
    else:
        return redirect('/')


def upload_photo(request, pk):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.post = Post.objects.get(id=pk)
            photo.save()
            return HttpResponseRedirect('/')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

