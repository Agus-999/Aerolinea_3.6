🎟️ Gestión de Reservas y Selección de Asientos

Un módulo del sistema de gestión de vuelos desarrollado en Django que permite a los empleados ver, crear, editar y eliminar reservas, así como asignar asientos con cálculo automático del precio total.

🚀 Funcionalidades principales

✈️ Lista de reservas con información del vuelo y pasajero
🆕 Crear nueva reserva con formulario unificado
✏️ Editar reserva y datos del pasajero asociados
💺 Selección interactiva de asientos con actualización de precio total
💰 Cálculo automático del precio por tipo de asiento
🗑️ Eliminar reserva con confirmación previa
🔒 Acceso exclusivo para empleados autenticados

📋 Detalle de funciones principales

Selección de Asientos:

Visualiza asientos disponibles, ocupados y asignados al empleado.

Muestra nombre, fila, columna, tipo y precio por asiento.

Actualización del total de forma inmediata al confirmar.

Detalle de Reserva:

Lista de asientos asignados con su precio individual.

Visualización del precio total de la reserva.

Posibilidad de modificar asientos y actualizar pasajero/vuelo.

📁 Estructura de archivos y carpetas
gestion/
├── migrations/
├── templates/
│   └── empleados/
│       └── reservas/
│           ├── detalle_reserva.html
│           ├── asientos.html
│           ├── lista.html
│           ├── eliminar.html
│           └── formulario.html
├── static/
│   └── (archivos estáticos: CSS, JS, imágenes)
├── forms.py
├── models.py
├── urls.py
├── views.py
└── tests.py

🔗 URLs principales
Ruta	Vista	Descripción
/empleados/reservas/	lista_reservas_empleado	Lista de todas las reservas
/empleados/reservas/nueva/	crear_reserva_empleado	Crear una nueva reserva
/empleados/reservas/<id>/	detalle_reserva_empleado	Ver y editar detalle de la reserva
/empleados/reservas/<id>/eliminar/	eliminar_reserva_empleado	Confirmar y eliminar una reserva
/empleados/reservas/<id>/asientos/	ver_asientos_empleado	Seleccionar o modificar asientos
/empleados/reservas/confirmar_asientos/	confirmar_compra_empleado	Guardar asientos seleccionados
🗃️ Modelos principales (models.py)

Reserva

relación con Pasajero

relación con Vuelo

relación con Asiento (M2M)

precio total calculado dinámicamente

Asiento

número, fila, columna

tipo (económico, primera, premium, etc.)

estado (disponible, ocupado)

relación con avión

⚙️ Lógica y flujo de trabajo

Autenticación obligatoria para todas las operaciones

Cálculo automático de precios en detalle_reserva_empleado y asientos.html

Actualización del total al confirmar selección

Reseteo de asientos y precios si cambia el vuelo en la reserva

Bloqueo de asientos ocupados para evitar conflictos

🖥️ Frontend y experiencia de usuario

Interfaz responsive con Bootstrap

Tabla de asientos con colores y estados claros

Checkbox para seleccionar asientos disponibles

Cálculo y visualización del total en el detalle de reserva

Alertas y mensajes claros en operaciones exitosas o con error

📦 Cómo poner en marcha este módulo

Clonar el proyecto principal y activar el entorno virtual

Ejecutar migraciones si hay cambios en modelos:

python manage.py makemigrations gestion
python manage.py migrate


Levantar el servidor local:

python manage.py runserver


Acceder a:

http://localhost:8000/empleados/reservas/

👨‍💻 Autor

Agustín Fasano
Estudiante de Desarrollo de Software en ITEC