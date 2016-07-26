from django.db import models
from imagekit.models import ImageSpecField

from common.models import UserProfile

from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class Post(models.Model):
    author = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        return Post's title
        :return self.title:
        """
        return self.title


class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = ProcessedImageField(upload_to='photos',
                                processors=[ResizeToFill(400, 400)],
                                format='JPEG',
                                options={'quality': 80})

    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(100, 100)],
                                     format='JPEG',
                                     options={'qulity': 60})

