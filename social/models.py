from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

"""
class Plunt(models.Model):
    # owner =  models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(max_length=200)
    # species = 
    # description

class Picture(models.Model):
    plunt = models.ForeignKey(Plunt, on_delete=models.SET_NULL, null=True)


class Species(models.Model):
    name = models.CharField(max_length=200)
"""