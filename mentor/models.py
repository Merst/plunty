from django.db import models

# Dimension table for patches
class Patch(models.Model):
    name = models.CharField(max_length=10)
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return self.name

# Dimension table representing the possible areas.
# Will require updates to the fields every patch

class Instance(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, default='N/A')

    def __str__(self):
        return self.name

# Fact table collecting every attempts of the Mentor roulette

class Attempt(models.Model):
    area = models.ForeignKey('Instance', on_delete=models.SET_NULL, null=True)
    date_submitted = models.DateField()
    success = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}. {self.area.name}'
