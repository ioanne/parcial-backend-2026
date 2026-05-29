from django.db import models

# Create your models here.

# from examen.models import AsignacionExamen
# from profesor.models import Profesor

# Modelo para guardar comentarios de profesores sobre las asignaciones de examen.
class Retroalimentacion(models.Model):

    # Asignación asociada al comentario
    # asignacion = models.ForeignKey(
    #     AsignacionExamen,
    #     on_delete=models.CASCADE,
    #     related_name='retroalimentaciones'
    # )

    # Profesor que realiza la retroalimentación
    # profesor = models.ForeignKey(
    #     Profesor,
    #     on_delete=models.CASCADE
    # )

    # Comentario o corrección escrita
    texto = models.TextField()

    # Fecha y hora de creación automática
    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        # Ordenar por fecha de creación
        ordering = ['fecha_creacion']

    def __str__(self):
        return f"Retroalimentacion {self.id}"