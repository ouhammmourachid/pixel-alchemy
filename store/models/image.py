import os

from django.conf import settings
from django.db import models
from django.utils import timezone

from .tag import Tag


def image_upload_path(instance, filename):
    """this function allow as to create the file name as combination of the timestamp and the original name"""
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f'image-{timestamp}{file_extension}'
    return f'images/{new_filename}'


class Image(models.Model):
    id = models.AutoField(primary_key=True)  # noqa: A003
    imagePath = models.ImageField(upload_to=image_upload_path)
    description = models.CharField(max_length=500, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    isPrivate = models.BooleanField(default=False)

    # Add other image fields here
    tags = models.ManyToManyField(Tag, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Image n° : {self.id} - {str(self.imagePath).split("/")[-1]}'

    def delete(self, *args, **kwargs):
        """Remove the image file from the filesystem"""
        if self.imagePath:
            image_path = os.path.join(settings.MEDIA_ROOT, str(self.imagePath))
            if os.path.exists(image_path):
                os.remove(image_path)

        super(Image, self).delete(*args, **kwargs)
