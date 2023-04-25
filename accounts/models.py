from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, default=None)
    is_staff = models.BooleanField(default=False)
