from django.forms import ModelForm

from blog.models import Post, Photo


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ('photo', )
