🧳 Gestión de Pasajeros
Un módulo del sistema de gestión de vuelos desarrollado en Django para que los empleados puedan ver, crear, editar y eliminar pasajeros de manera sencilla y segura.

🚀 Funcionalidades principales
👤 Lista de pasajeros con información completa

📝 Crear nuevo pasajero desde formulario unificado

✏️ Editar pasajero usando el mismo formulario de creación

🗑️ Eliminar pasajero con confirmación previa

🔒 Acceso exclusivo para empleados autenticados

📋 Detalle completo del pasajero con todos sus datos de contacto

📁 Estructura de archivos y carpetas
gestion/
├── migrations/
├── templates/
│ └── empleados/
│ └── pasajeros/
│ ├── detalle.html
│ ├── eliminar.html
│ ├── formulario.html
│ └── lista.html
├── static/
│ └── (archivos estáticos: CSS, JS, imágenes)
├── forms.py
├── models.py
├── urls.py
├── views.py
└── tests.py

🔗 URLs principales
Ruta	Vista	Descripción
/pasajeros/	lista_pasajeros	Lista de todos los pasajeros
/pasajeros/nuevo/	nuevo_pasajero	Crear un nuevo pasajero
/pasajeros/<id>/editar/	editar_pasajero	Editar datos de un pasajero existente
/pasajeros/<id>/eliminar/	eliminar_pasajero	Confirmar y eliminar un pasajero
/pasajeros/<id>/	detalle_pasajero	Ver detalle completo del pasajero

🗃️ Modelo principal (models.py)
Pasajero
usuario (opcional) → relación con el usuario autenticado

nombre, documento, email, telefono

fecha_nacimiento, tipo_documento (DNI, Pasaporte, Otro)

Método __str__() para mostrar el nombre en interfaces y listas

⚙️ Lógica y flujo de trabajo
Autenticación obligatoria para todas las operaciones

Validaciones de formulario para datos completos y correctos

Edición y creación usan el mismo formulario (formulario.html)

Eliminación solicita confirmación antes de borrar el registro

Acceso restringido solo a personal autorizado

🖥️ Frontend y experiencia de usuario
Interfaz clara y responsive con Bootstrap

Listado con tabla o grid según necesidad

Formulario de creación/edición con campos obligatorios destacados

Alertas y mensajes para feedback inmediato

Confirmación visual al eliminar un pasajero

📦 Cómo poner en marcha este módulo
Asegurarse de tener el proyecto principal clonado y virtualenv activado

Ejecutar migraciones si hay cambios en Pasajero:

bash
Copiar código
python manage.py makemigrations gestion
python manage.py migrate
Levantar servidor local:

bash
Copiar código
python manage.py runserver
Acceder a: http://localhost:8000/pasajeros/ para ver el listado

👨‍💻 Autor
Agustín Fasano
Estudiante de Desarrollo de Software en ITEC