from django.db import models


class Tag(models.Model):
    id = models.AutoField(primary_key=True)  # noqa:A003
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
