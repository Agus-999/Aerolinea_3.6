# ✈️ Sistema de Gestión de Vuelos - Aerolínea

Este es un proyecto de gestión de vuelos desarrollado en Django. Permite el **registro**, **inicio de sesión** y control de acceso según el rol del usuario.  
🔒 Solo los usuarios autenticados podrán acceder a las funcionalidades internas del sistema.

---

## 🚀 Etapa 3 - Subetapa 1: Registro e Inicio de Sesión

### ✅ Objetivo

Implementar:
- Registro de usuarios con rol (`admin`, `empleado`, etc.).
- Inicio de sesión.
- Restricción de acceso a usuarios autenticados.
- Visualización del nombre y rol en la barra de navegación.
- Vista de inicio protegida.

---

## 🛠️ Pasos realizados

### 1️⃣ Modelo personalizado de Usuario

📄 `home/models.py`

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    rol = models.CharField(max_length=20, default='empleado')
Este modelo permite almacenar el rol de cada usuario.

2️⃣ Registro de modelo en admin
📄 home/admin.py

python
Copiar código
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
3️⃣ Formulario de registro
📄 home/forms.py

python
Copiar código
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'rol']
4️⃣ Vistas
📄 home/views.py

python
Copiar código
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def inicio(request):
    return render(request, 'inicio.html')
5️⃣ URLs
📄 home/urls.py

python
Copiar código
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
📄 aerolinea/urls.py

python
Copiar código
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
6️⃣ Templates
📄 templates/base.html

html
Copiar código
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Aerolínea{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'inicio' %}">Inicio</a> |

        {% if user.is_authenticated %}
            <p>Hola, {{ user.username }} ({{ user.rol }})</p>
            <a href="{% url 'logout' %}">Cerrar sesión</a>
        {% else %}
            <a href="{% url 'login' %}">Iniciar sesión</a> |
            <a href="{% url 'register' %}">Registrarse</a>
        {% endif %}
    </nav>

    <hr>

    {% block content %}
    {% endblock %}
</body>
</html>
📄 templates/register.html

html
Copiar código
{% extends 'base.html' %}

{% block title %}Registro - Aerolínea{% endblock %}

{% block content %}
<h2>Registro</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Registrarse</button>
</form>
{% endblock %}
📄 templates/login.html

html
Copiar código
{% extends 'base.html' %}

{% block title %}Iniciar sesión - Aerolínea{% endblock %}

{% block content %}
<h2>Iniciar sesión</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
</form>
{% endblock %}
📄 templates/inicio.html

html
Copiar código
{% extends 'base.html' %}

{% block title %}Inicio - Aerolínea{% endblock %}

{% block content %}
    <h2>Bienvenido al sistema de gestión de vuelos</h2>
    <p>Desde aquí podrás acceder a todas las funcionalidades.</p>
{% endblock %}
🧠 Consideraciones
Se utiliza CustomUser para personalizar el modelo y agregar el campo rol.

La vista de inicio está protegida con @login_required.

Si se crea un superusuario con createsuperuser, se le puede asignar el rol de 'admin' desde el panel admin o manualmente.

👤 Autor
Agustín Fasano
💻 Desarrollador de Software | Estudiante en ITEC
🗂️ Proyecto para práctica de autenticación y roles en Django

