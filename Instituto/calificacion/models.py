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

class AsignacionExamen(models.Model):
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    calificacion = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    observaciones = models.TextField(blank=True)

    # examen = models.ForeignKey('examen.Examen', on_delete=models.CASCADE)
    # alumno = models.ForeignKey('alumno.Alumno', on_delete=models.CASCADE)

    def __str__(self):
        return f"Asignacion #{self.id} - Nota: {self.calificacion}"  # Create your models here.
