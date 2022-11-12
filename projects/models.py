from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

# Enumeration of technical skills related to a project.
class Skill(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the name of the technical skill.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    skill = models.ManyToManyField(Skill, help_text='Select the appropriate related technical skills')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the project')
    github_link = models.URLField(max_length=200)    

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    """
    def get_absolute_url(self):
        # Returns the URL to access a detail record for this book.
        return reverse('book-detail', args=[str(self.id)])
    """
