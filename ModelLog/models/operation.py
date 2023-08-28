from django.db import models

from store.models import Image


class Operation(models.Model):
    OPERATION_NAMES = [
        ('arbitrary-image-stylization-v1-256/2', 'neural-style-transfer-v2'),
    ]
    id = models.AutoField(primary_key=True)  # noqa:A003
    operation = models.CharField(max_length=255, choices=OPERATION_NAMES)
    firstImage = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='first_image_operations')
    secondImage = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='second_image_operations', blank=True
    )

    def __str__(self):
        return f"""
        Operation n° : {self.id} - {self.operation} On Image {self.firstImage_id} and Image {self.secondImage_id}
        """
