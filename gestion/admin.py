from django.contrib import admin
from .models import Avion, Vuelo, Pasajero, Reserva, Asiento, Boleto


# Admin para Avion
@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'capacidad', 'filas', 'columnas')
    search_fields = ('modelo',)


# Admin para Vuelo
@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino', 'fecha_salida', 'fecha_llegada', 'estado', 'mostrar_duracion')
    search_fields = ('origen', 'destino')

    def mostrar_duracion(self, obj):
        return str(obj.duracion) if obj.duracion else "No calculada"
    mostrar_duracion.short_description = 'Duración'


# Admin para Pasajero
@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'documento', 'get_tipo_documento', 'get_email', 'get_telefono', 'get_fecha_nacimiento')
    search_fields = ('nombre', 'documento', 'usuario__email')

    def get_tipo_documento(self, obj):
        return obj.tipo_documento
    get_tipo_documento.short_description = 'Tipo Documento'

    def get_email(self, obj):
        return obj.usuario.email
    get_email.short_description = 'Email'

    def get_telefono(self, obj):
        return obj.usuario.telefono
    get_telefono.short_description = 'Teléfono'

    def get_fecha_nacimiento(self, obj):
        return obj.usuario.fecha_nacimiento
    get_fecha_nacimiento.short_description = 'Fecha Nacimiento'


# Admin para Asiento
@admin.register(Asiento)
class AsientoAdmin(admin.ModelAdmin):
    list_display = ('avion', 'numero', 'fila', 'columna', 'tipo', 'estado')
    search_fields = ('avion__modelo', 'numero')


# Admin para Reserva
# @admin.register(Reserva)
# class ReservaAdmin(admin.ModelAdmin):
#     list_display = ('codigo_reserva', 'vuelo', 'pasajero', 'asiento', 'estado', 'fecha_reserva', 'precio')
#     search_fields = ('codigo_reserva', 'pasajero__nombre', 'vuelo__origen', 'vuelo__destino')


# Admin para Boleto
@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('codigo_barra', 'reserva', 'fecha_emision', 'estado')
    search_fields = ('codigo_barra', 'reserva__codigo_reserva')
