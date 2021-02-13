
from django.db import models

class Personas(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    CheckIn = models.CharField(max_length=20, default='DEFAULT VALUE')
    CheckOut = models.CharField(max_length=100, default='DEFAULT VALUE')
 
    class Meta:
         db_table = 'personas'