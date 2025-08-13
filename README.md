🎟️ Gestión de Boletos de Vuelos
Extensión del sistema de reservas de vuelos en Django, ahora con boletos generados automáticamente al crear una reserva y posibilidad de descargarlos en formato HTML imprimible.

🚀 Funcionalidades principales de Boletos
🛬 Generación automática de boletos al crear una reserva

🆔 Cada boleto tiene un código de barra único

📅 Registro de fecha de emisión

🔖 Estado del boleto: emitido o cancelado

🖨️ Descarga del boleto en formato HTML listo para imprimir desde el detalle de la reserva

🔄 Integración completa con la reserva y los asientos asignados

📁 Estructura de archivos y carpetas relacionada
gestion/
├── templates/
│ └── clientes/
│ └── boletos/
│ └── boleto.html ← plantilla para visualización/descarga del boleto
├── views.py ← vista descargar_boleto
├── models.py ← modelo Boleto
├── urls.py ← ruta descargar_boleto

🔗 URLs principales relacionadas con boletos
Ruta	Vista	Descripción
/reservas/<reserva_id>/boleto/descargar/	descargar_boleto	Mostrar y descargar el boleto asociado a la reserva

🗃️ Modelo principal: Boleto (models.py)
reserva → Relación OneToOne con la reserva correspondiente

codigo_barra → Código de identificación único del boleto

fecha_emision → Fecha de creación automática

estado → 'emitido' o 'cancelado'

Métodos básicos: __str__() para mostrar de forma legible

⚙️ Lógica y flujo de boletos
Cuando se crea una reserva, automáticamente se genera un boleto vinculado

Si por alguna razón no existe el boleto, se crea al acceder a la vista de descarga (descargar_boleto)

La descarga es mediante renderizado HTML, listo para imprimir o guardar como PDF desde el navegador

Mantiene integridad con los asientos reservados y el usuario autenticado

🖥️ Frontend y experiencia de usuario
Se integra en el detalle de la reserva (detalle.html) con botón: 🎟️ Descargar Boleto

Interfaz limpia y responsiva

Muestra información completa: código de barra, fecha de emisión, datos del pasajero y asientos

Fácil de imprimir o guardar en PDF desde el navegador

📦 Cómo probar la funcionalidad
Crear una reserva desde /reservas/crear/

Ir al detalle de la reserva (/reservas/<reserva_id>/)

Hacer clic en 🎟️ Descargar Boleto

Verás el boleto generado automáticamente listo para imprimir

👨‍💻 Autor
Agustín Fasano
Estudiante de Desarrollo de Software en ITEC