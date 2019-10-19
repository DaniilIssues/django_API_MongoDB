from django.contrib.auth.models import AbstractUser
from django.db import models


class CUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars_users/', blank=True)
    date_birth = models.DateField(blank=True)