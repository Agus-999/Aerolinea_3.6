from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
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
    path('pasajeros/<int:pasajero_id>/', views.detalle_pasajero, name='detalle_pasajero'),

   # CLIENTES – VUELOS
    path('clientes/vuelos/', views.vuelos_clientes_lista, name='vuelos_clientes_lista'),
    path('clientes/vuelos/<int:pk>/', views.vuelos_clientes_detalle, name='vuelos_clientes_detalle'),

    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),

path('reservas/crear/', views.crear_reserva, name='crear_reserva'),

path('reservas/<int:reserva_id>/', views.detalle_reserva, name='detalle_reserva'),
path('reservas/<int:reserva_id>/editar/', views.editar_reserva, name='editar_reserva'),

path('reservas/<int:reserva_id>/eliminar/', views.eliminar_reserva, name='eliminar_reserva'),

path('reservas/<int:reserva_id>/asientos/', views.ver_asientos, name='ver_asientos'),

path('confirmar-compra/', views.confirmar_compra, name='confirmar_compra'),

]

