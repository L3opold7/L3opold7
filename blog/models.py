from django.db import models
from common.models import UserProfile
from django.utils import timezone


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