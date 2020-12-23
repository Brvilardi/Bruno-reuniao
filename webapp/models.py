from django.db import models

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=6, default="SIM")
