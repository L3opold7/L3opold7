from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
