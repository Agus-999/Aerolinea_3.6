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

   # CLIENTES – VUELOS
    path('clientes/vuelos/', views.vuelos_clientes_lista, name='vuelos_clientes_lista'),
    path('clientes/vuelos/<int:pk>/', views.vuelos_clientes_detalle, name='vuelos_clientes_detalle'),
]
