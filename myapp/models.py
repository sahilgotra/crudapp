from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class register(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=100)

  def __str__(self):
    return self.firstname