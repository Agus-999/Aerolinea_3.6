from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    # EMPLEADOS
    path('aviones/', views.lista_aviones, name='lista_aviones'),
    path('aviones/nuevo/', views.nuevo_avion, name='nuevo_avion'),
    path('aviones/<int:pk>/editar/', views.editar_avion, name='editar_avion'),
    path('aviones/<int:pk>/eliminar/', views.eliminar_avion, name='eliminar_avion'),
    path('avion/<int:pk>/', views.detalle_avion, name='detalle_avion'),

    path('vuelos/', views.lista_vuelos, name='lista_vuelos'),
    path('vuelos/nuevo/', views.crear_vuelo, name='crear_vuelo'),
    path('vuelos/<int:pk>/editar/', views.editar_vuelo, name='editar_vuelo'),
    path('vuelos/<int:pk>/eliminar/', views.eliminar_vuelo, name='eliminar_vuelo'),

    path('pasajeros/', views.lista_pasajeros, name='lista_pasajeros'),
    path('pasajeros/nuevo/', views.nuevo_pasajero, name='nuevo_pasajero'),
    path('pasajeros/<int:pasajero_id>/editar/', views.editar_pasajero, name='editar_pasajero'),
    path('pasajeros/<int:pasajero_id>/eliminar/', views.eliminar_pasajero, name='eliminar_pasajero'),

    path('empleados/reservas/', views.lista_reservas_empleado, name='lista_reservas_empleado'),
    path('empleados/reservas/nueva/', views.crear_reserva_empleado, name='crear_reserva_empleado'),
    path('empleados/reservas/<int:reserva_id>/', views.detalle_reserva_empleado, name='detalle_reserva_empleado'),
    path('empleados/reservas/<int:reserva_id>/eliminar/', views.eliminar_reserva_empleado, name='eliminar_reserva_empleado'),
    path('empleados/reservas/<int:reserva_id>/asientos/', views.ver_asientos_empleado, name='ver_asientos_empleado'),
    path('empleados/reservas/confirmar_asientos/', views.confirmar_compra_empleado, name='confirmar_compra_empleado'),

    path('empleados/boletos/', views.lista_boletos_empleado, name='lista_boletos_empleado'),
    path('empleados/boletos/verificar/<str:codigo>/', views.verificar_boleto_empleado, name='verificar_boleto_empleado'),

    path('empleados/asientos/', views.panel_asientos_empleados, name='panel_asientos_empleados'),
    path('empleados/asientos/cambiar_estado/', views.cambiar_estado_asiento, name='cambiar_estado_asiento'),
    
    path('empleados/asientos/', views.panel_asientos_empleados, name='panel_asientos_empleados'),
    path('empleados/asientos/cambiar_estado/', views.cambiar_estado_asiento, name='cambiar_estado_asiento'),
    path('empleados/reservas/', views.lista_reservas_empleado, name='lista_reservas_empleado'),
    path('empleados/reporte_reservas/', views.reporte_reservas, name='reporte_reservas'),  # <- NUEVA

   # CLIENTES
    path('clientes/vuelos/', views.vuelos_clientes_lista, name='vuelos_clientes_lista'),
    path('clientes/vuelos/<int:pk>/', views.vuelos_clientes_detalle, name='vuelos_clientes_detalle'),

    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    path('reservas/<int:reserva_id>/', views.detalle_reserva, name='detalle_reserva'),
    path('reservas/<int:reserva_id>/editar/', views.editar_reserva, name='editar_reserva'),
    path('reservas/<int:reserva_id>/eliminar/', views.eliminar_reserva, name='eliminar_reserva'),
    path('reservas/<int:reserva_id>/asientos/', views.ver_asientos, name='ver_asientos'),
    path('confirmar-compra/', views.confirmar_compra, name='confirmar_compra'),

    # ✅ Nueva: ver/descargar boleto (HTML imprimible a PDF)
    path('reservas/<int:reserva_id>/boleto/descargar/', views.descargar_boleto, name='descargar_boleto'),

    path('reservas/<int:reserva_id>/boleto/', views.ver_boleto, name='ver_boleto'),
    path('reservas/<int:reserva_id>/boleto/descargar/', views.descargar_boleto, name='descargar_boleto'),
    
]

