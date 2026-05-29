from django.contrib import admin

from .models import AsignacionExamen

# Register your models here.
from .models import Retroalimentacion


@admin.register(Retroalimentacion)
class RetroalimentacionAdmin(admin.ModelAdmin):

    # Campos visibles en la lista del admin
    list_display = (
        'id',
        # 'asignacion',
        # 'profesor',
        'fecha_creacion'
    )

    # Permite buscar por texto del comentario
    search_fields = (
        'texto',
    )

    # Agrega filtro por fecha de creación
    list_filter = (
        'fecha_creacion',
    )
 
     # Optimiza consultas relacionadas
    list_select_related = (
    # 'asignacion',
    # 'profesor',
)

admin.site.register(AsignacionExamen)
