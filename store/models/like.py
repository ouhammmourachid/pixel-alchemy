from django.conf import settings
from django.db import models

from .image import Image


class Like(models.Model):
    id = models.AutoField(primary_key=True)  # noqa:A003
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imageId = models.ForeignKey(Image, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like {self.id} by User {self.userId_id} on Image {self.imageId_id}'
