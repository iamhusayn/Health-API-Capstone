from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  ROLE_CHOICES = (
    ('regular1', 'Guardian'),
    ('assigner', 'Doctor'),
    ('regular2', 'Patient'),
  )

  username = None
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  category = models.CharField(max_length=40, choices=ROLE_CHOICES, blank=False, null=False, default='regular2')

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  def __str__(self):
    return self.email

# class Login(models.Model):
#   username = models.CharField(max_length=100)
#   email = models.EmailField(default='')