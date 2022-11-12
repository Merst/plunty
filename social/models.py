from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class Plunt():
    # owner = 
    nickname = models.CharField(max_length=200)
    # species = 
    # description

class Picture():
    plunt = models.ForeignKey(Plunt, on_delete=models.SET_NULL, null=True)



class Species():
    name = models.CharField(max_length=200)