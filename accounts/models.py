from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Account(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True, verbose_name='Email')
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email