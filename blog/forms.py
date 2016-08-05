from django import forms

from blog.models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('photo', )


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

