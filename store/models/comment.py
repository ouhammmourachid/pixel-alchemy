from django.conf import settings
from django.db import models

from .image import Image


class Comment(models.Model):
    id = models.AutoField(primary_key=True)  # noqa:A003
    createdAt = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment n° : {self.id} - made by user {self.user_id} on image {self.image_id}'
