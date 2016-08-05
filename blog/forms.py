from django import forms

from .models import Post, Photo


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', )


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('photo', )
