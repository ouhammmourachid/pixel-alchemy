from django.conf import settings
from django.db import models

from .image import Image


class Comment(models.Model):
    id = models.AutoField(primary_key=True)  # noqa:A003
    createdAt = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imageId = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment {self.id}: {self.text}'
