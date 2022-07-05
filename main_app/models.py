from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField()
    generation = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    evolution_stage = models.IntegerField()