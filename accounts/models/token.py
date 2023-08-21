from django.db import models

from .user import User


class Token(models.Model):
    id = models.AutoField(primary_key=True)  # noqa: A003
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token
