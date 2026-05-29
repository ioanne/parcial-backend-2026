from django.db import models


class AsignacionExamen(models.Model):
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    calificacion = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    observaciones = models.TextField(blank=True)

    # examen = models.ForeignKey('core.Examen', on_delete=models.CASCADE)
    # alumno = models.ForeignKey('core.Alumno', on_delete=models.CASCADE)

    def __str__(self):
        return f"Asignacion #{self.id} - Nota: {self.calificacion}"  # Create your models here.
