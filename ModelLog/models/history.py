from django.conf import settings
from django.db import models

from store.models import Image

from .operation import Operation


class History(models.Model):
    id = models.AutoField(primary_key=True)  # noqa:A003
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resultImage = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='result_image_histories')
    operationId = models.ForeignKey(Operation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Log-n°{self.id}-{self.timestamp}-{self.operationId.id}'
