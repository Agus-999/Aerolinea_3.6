✈️ Etapa 4 - Subetapa 1: Gestión de Aviones - Portal para Empleados 🧑‍✈️
En esta subetapa se implementó una interfaz para que empleados autenticados puedan gestionar aviones desde el sistema. Esto incluye registrar, modificar, listar y eliminar aviones desde el panel web.

🔐 Solo los usuarios con rol empleado pueden acceder a esta funcionalidad.

🛫 Escala del Proyecto
Etapa 4: Funcionalidades por Rol
├── 🟢 Subetapa 1: Gestión de Aviones (actual)
└── 🔵 Subetapa 2: [pendiente]

🎯 Objetivo de esta Subetapa
Permitir a los empleados agregar, editar y eliminar aviones.

Crear una sección con listado en tabla.

Asegurar que esta función solo esté disponible para usuarios con rol empleado.

Agregar campos clave como modelo, capacidad, filas y columnas.

🛠️ Cambios Realizados
🛩️ 1. Modelo Avion
📄 gestion/models.py

python
Copiar código
class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField(default=1)
    columnas = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.modelo
🧾 2. Formulario de Aviones
📄 gestion/forms.py

python
Copiar código
class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['modelo', 'capacidad', 'filas', 'columnas']
🧠 3. Lógica de Vistas
📄 gestion/views.py
Incluye lógica para listar, crear, editar y eliminar aviones.

lista_aviones: muestra una tabla con los datos.

avion_formulario: se reutiliza para crear y editar.

eliminar_avion: confirma y elimina un avión.

🌐 4. URLs para CRUD
📄 gestion/urls.py

python
Copiar código
urlpatterns = [
    path('aviones/', views.lista_aviones, name='lista_aviones'),
    path('aviones/nuevo/', views.avion_formulario, name='nuevo_avion'),
    path('aviones/<int:pk>/editar/', views.avion_formulario, name='editar_avion'),
    path('aviones/<int:pk>/eliminar/', views.eliminar_avion, name='eliminar_avion'),
]
🧑‍✈️ 5. Interfaz Web para Empleados
📂 empleados/aviones/

lista.html: muestra todos los aviones en una tabla.

formulario.html: contiene el formulario para agregar o editar.

eliminar.html: página de confirmación para eliminar.

La navegación hacia esta sección solo se muestra si el usuario tiene el rol empleado.

💼 6. Administración en Django
📄 gestion/admin.py

python
Copiar código
@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'capacidad', 'filas', 'columnas')
    search_fields = ('modelo',)
🧭 7. Integración en el Template Base
📄 templates/base.html

django
Copiar código
{% if user.is_authenticated and user.rol == "empleado" %}
    <a href="{% url 'gestion:lista_aviones' %}">Gestión Aviones</a> |
{% endif %}
Esto asegura que solo los empleados vean el acceso a la gestión de aviones.

🗂️ Archivos Clave Modificados
Archivo	Descripción
models.py	Define el modelo Avion
views.py	Lógica CRUD para aviones
forms.py	Formulario para aviones
urls.py	Rutas para la gestión
admin.py	Registro en el panel Django
base.html	Control de acceso por rol
templates/empleados/aviones/	Interfaz de usuario

👨‍💼 Autor
Agustín Fasano
🎓 Estudiante ITEC | 💻 Desarrollador en formación
📁 Proyecto académico de gestión aeronáutica con Django