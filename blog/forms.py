from django import forms

from .models import Post, Photo


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tag']

    title = forms.CharField(label='title', max_length=30)
    content = forms.CharField(label='content')
    tag = forms.CharField(label='tag', max_length=20)


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('photo', )
