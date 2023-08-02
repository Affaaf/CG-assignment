from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, validators=[validate_email], null=False)
    username = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email