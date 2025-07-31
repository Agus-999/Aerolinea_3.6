from django.contrib import admin
from .models import Avion

@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'capacidad', 'filas', 'columnas')
    search_fields = ('modelo',)

from django.contrib import admin
from .models import Avion, Vuelo
from datetime import timedelta

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino', 'fecha_salida', 'fecha_llegada', 'estado', 'mostrar_duracion')
    search_fields = ('origen', 'destino')

    def mostrar_duracion(self, obj):
        return str(obj.duracion) if obj.duracion else "No calculada"
    mostrar_duracion.short_description = 'Duración'
