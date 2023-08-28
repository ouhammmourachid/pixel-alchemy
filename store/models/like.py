from django.conf import settings
from django.db import models

from .image import Image


class Like(models.Model):
    id = models.AutoField(primary_key=True)  # noqa:A003
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Add a unique constraint to ensure a user can only like an image once
        unique_together = ('user', 'image')

    def __str__(self):
        return f'Like n° : {self.id} - by User {self.user_id} on Image {self.image_id}'
