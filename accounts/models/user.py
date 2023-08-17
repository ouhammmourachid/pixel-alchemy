from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLES)
    is_active = models.BooleanField(default=True)
    REQUIRED_FIELDS: List[str] = []
