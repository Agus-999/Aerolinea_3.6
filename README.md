🛫 Reporte de Reservas y Gestión de Asientos – Módulo para Empleados

Un módulo del sistema de gestión de vuelos desarrollado en Django, diseñado para que los empleados puedan visualizar todas las reservas, filtrar por vuelo o pasajero y ver los asientos asignados de manera clara, incluyendo las reservas que todavía no tienen asientos asignados.

🚀 Funcionalidades principales
📊 Reporte de Reservas

Visualización de todas las reservas con información detallada:

Vuelo (origen, destino y fecha)

Pasajero (nombre y documento)

Asientos asignados (si los tiene)

Estado de la reserva (Confirmada, Pendiente, Ocupado)

Fecha de reserva

Precio total

Filtrado de reservas por:

Vuelo

Nombre del pasajero

Detección de reservas sin asientos asignados, mostrando “No asignado” para estas.

💺 Gestión de Asientos

Las reservas que tienen asientos asignados muestran los números correspondientes.

Las reservas pendientes o sin asignación de asientos se identifican claramente en el reporte.

Evita duplicados de reservas cuando se usan filtros o se listan varias relaciones ManyToMany de asientos.

📁 Estructura de archivos y carpetas
gestion/
├── templates/
│   └── empleados/
│       └── reservas/
│           └── reporte_reservas.html   # Plantilla HTML del reporte
├── models.py                             # Modelos Reserva, Vuelo, Asiento
├── views.py                              # Lógica de la vista reporte_reservas

🔗 Flujo de reporte

El empleado accede a la sección de Reporte de Reservas en el sistema.

La vista reporte_reservas obtiene todas las reservas y sus relaciones (vuelo, pasajero, usuario y asientos).

Se aplican filtros opcionales por vuelo o nombre del pasajero.

La plantilla HTML muestra:

Todos los datos de la reserva

Asientos asignados o “No asignado” si la reserva no tiene asientos

Estado y precio

Los empleados pueden ver rápidamente cuáles reservas necesitan asignación de asientos y cuáles están confirmadas.

🗃️ Modelo de datos utilizado (models.py)
Reserva

Información del pasajero, vuelo y estado.

Relación ManyToMany con Asiento.

Precio total de la reserva.

Asiento

Número de asiento

Relación con la reserva

Puede no estar asignado a algunas reservas pendientes.

Vuelo

Origen y destino

Fecha y hora de salida

Relación con reservas existentes

⚙️ Lógica y flujo de trabajo

Se utilizan select_related y prefetch_related para optimizar la carga de datos de relaciones.

El reporte detecta automáticamente reservas sin asientos asignados.

La plantilla HTML es dinámica, mostrando claramente los datos de cada reserva.

El filtro de vuelo utiliza los objetos Vuelo reales para mostrar origen, destino y fecha.

Las reservas duplicadas por asientos M2M se eliminan con .distinct().

🖥️ Frontend y experiencia del empleado

Plantilla HTML optimizada para lectura rápida en escritorio.

Tabla con columnas:

Vuelo

Pasajero

Documento

Asientos

Estado

Fecha de reserva

Precio

Estilo claro y moderno, con colores que diferencian estados de reserva.

Filtros fáciles de usar para agilizar la búsqueda de reservas específicas.

📦 Cómo poner en marcha este módulo

Asegurarse que las relaciones Reserva → Asiento → Vuelo → Pasajero estén correctamente definidas en models.py.

Colocar la plantilla reporte_reservas.html en templates/empleados/reservas/.

Configurar las rutas en urls.py para que los empleados puedan acceder al reporte.

Ejecutar el servidor con python manage.py runserver y verificar:

Listado de reservas

Filtro por vuelo y pasajero

Visualización correcta de asientos asignados o “No asignado” cuando corresponde

👨‍💻 Autor

Agustín Fasano
Estudiante de Desarrollo de Software en ITEC