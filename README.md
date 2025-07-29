# 🛡️ Etapa 3 - Subetapa 2: Acceso de Administrador - Sistema de Gestión de Vuelos ✈️

Esta etapa mejora el sistema permitiendo que el **usuario con rol `admin`** tenga acceso completo al panel de administración de Django, y pueda gestionar todos los usuarios desde allí.

🔐 Solo los usuarios autenticados y con rol `admin` podrán ver el enlace al panel administrativo.

---

## 📈 Escala del Proyecto

Etapa 3: Sistema de Autenticación y Roles
├── 🟢 Subetapa 1: Registro e Inicio de Sesión
└── 🔵 Subetapa 2: Acceso de Administrador (actual)

yaml
Copiar
Editar

---

## 🎯 Objetivo de esta Subetapa

- Mostrar la opción de acceso al panel **/admin** solo a usuarios con rol `admin`.
- Registrar correctamente el modelo personalizado `Usuario` en el admin.
- Permitir gestión total de los usuarios desde el panel de administración.

---

## 🧩 Cambios Realizados

### 1️⃣ Modelo de Usuario con Rol (ya implementado)

📄 `home/models.py`

from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
        ('cliente', 'Cliente'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='cliente')

    def __str__(self):
        return f"{self.username} ({self.rol})"
2️⃣ Registro del Modelo en el Panel de Administración
📄 home/admin.py

python
Copiar
Editar
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'email', 'rol', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        ('Rol Personalizado', {'fields': ('rol',)}),
    )
Este registro permite que el admin tenga control total desde el panel.

3️⃣ Condicional en Template para Mostrar Enlace al Admin
📄 templates/base.html

html
Copiar
Editar
<nav>
    <a href="{% url 'inicio' %}">Inicio</a> |

    {% if user.is_authenticated %}
        <a href="{% url 'logout' %}">Cerrar sesión</a>

        {% if user.rol == 'admin' %}
            | <a href="/admin/">Panel Admin</a>
        {% endif %}
    {% else %}
        <a href="{% url 'login' %}">Iniciar sesión</a> |
        <a href="{% url 'register' %}">Registrarse</a>
    {% endif %}
</nav>

{% if user.is_authenticated %}
  <div style="padding: 1rem; background-color: #f0f0f0; text-align: right;">
    <p>Hola, {{ user.username }} ({{ user.rol }})</p>
  </div>
{% endif %}
🔎 De esta forma, el enlace al panel de administración es visible solo si el usuario tiene el rol 'admin'.

📂 Archivos Clave Modificados
models.py → modelo Usuario con campo rol.

admin.py → registro del modelo para gestión completa en Django Admin.

base.html → condiciones para mostrar enlaces según autenticación y rol.

👨‍💼 Autor
Agustín Fasano
💻 Desarrollador de Software | Estudiante en ITEC
📚 Proyecto académico de autenticación y control de usuarios en Django