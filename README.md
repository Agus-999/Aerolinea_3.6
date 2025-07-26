# 🏠 Etapa 2: Creación de la app home y estructura base de la web

## 🧩 Creación de la app principal (home)

Creamos una nueva app dentro del proyecto Django para manejar la parte principal del sitio:

python manage.py startapp home
🧠 Registro de la app en Django
Agregamos 'home' a la lista de INSTALLED_APPS en el archivo settings.py:

python
Copiar código
INSTALLED_APPS = [
    ...
    'home',
]
🌐 Configuración de rutas
En ChatProject/urls.py, incluimos las URLs de la app home:

python
Copiar código
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
Creamos el archivo home/urls.py con la ruta base para la vista de inicio:

python
Copiar código
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
🖼️ Creación de vistas y plantillas
En home/views.py, definimos la vista inicio:

python
Copiar código
from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')
Creamos la carpeta templates/ dentro de la app home y las siguientes plantillas:

arduino
Copiar código
home/
└── templates/
    ├── base.html
    └── inicio.html
base.html
html
Copiar código
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Chat Anónimo</title>
</head>
<body>
    {% block contenido %}
    {% endblock %}
</body>
</html>
inicio.html
django
Copiar código
{% extends 'base.html' %}

{% block contenido %}
    <h1>Bienvenido al Chat Anónimo</h1>
{% endblock %}
✅ Verificación del funcionamiento
Ejecutamos el servidor de desarrollo para comprobar que la vista de inicio carga correctamente:

bash
Copiar código
python manage.py runserver
🗂️ Estructura actual del proyecto
markdown
Copiar código
chat-anonimo/
├── ChatProject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   └── inicio.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── venv/
✍️ Autor
Agustín Alejandro Fasano