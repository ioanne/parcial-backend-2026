from django.db import models

class asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    