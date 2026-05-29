from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    código = models.IntegerField()
    descripción = models.CharField(max_length=100)
