from django.db import models


class Examen(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Pregunta(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    examen = models.ForeignKey(
        Examen,
        on_delete=models.CASCADE,
        related_name="preguntas"
    )

    def __str__(self):
        return self.titulo


class Respuesta(models.Model):
    texto = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)

    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        related_name="respuestas"
    )

    def __str__(self):
        return self.texto