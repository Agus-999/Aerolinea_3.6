from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    path('aviones/', views.lista_aviones, name='lista_aviones'),
    path('aviones/nuevo/', views.avion_formulario, name='nuevo_avion'),
    path('aviones/<int:pk>/editar/', views.avion_formulario, name='editar_avion'),
    path('aviones/<int:pk>/eliminar/', views.eliminar_avion, name='eliminar_avion'),
]
