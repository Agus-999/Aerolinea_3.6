📧 Envío de Boletos por Correo – Módulo Automático

Un módulo del sistema de gestión de vuelos desarrollado en Django, que envía automáticamente por correo electrónico el boleto de vuelo al pasajero una vez confirmada su reserva.

🚀 Funcionalidades principales

📩 Generación automática de boletos en HTML con datos completos de la reserva:

Nombre y datos de contacto del pasajero

Código de boleto y código de reserva

Origen, destino, fecha y hora de vuelo

Lista de asientos asignados con su tipo y precio

Precio total de la reserva

📨 Envío automático del correo electrónico al email del pasajero después de completar la compra.

💡 Plantilla HTML personalizada con diseño claro y ordenado para una mejor experiencia del pasajero.

🔄 Adaptación dinámica del contenido del mail para mostrar correctamente los precios de los asientos según su tipo (económico, ejecutivo, primera clase, premium, etc.).

📁 Estructura de archivos y carpetas

gestion/
├── templates/
│   └── boletos/
│       └── boleto_email.html   # Plantilla HTML del correo
├── utils/
│   └── enviar_boleto.py        # Función para generar y enviar el mail
├── models.py                   # Modelos de Reserva, Asiento y Boleto
├── views.py                    # Lógica para disparar el envío del mail


🔗 Flujo de envío de correo

El pasajero realiza la reserva en el sistema.

Una vez confirmada, se generan:

Datos de la reserva

Lista de asientos con tipo y precio (usando el diccionario PRECIOS_ASIENTO)

Se renderiza la plantilla boleto_email.html con todos los datos.

Se envía el correo usando la función send_mail de Django, con el HTML embebido.

El pasajero recibe su boleto directamente en su bandeja de entrada.

🗃️ Modelo de datos utilizado (models.py)

Reserva
Contiene información del pasajero, vuelo, asientos y precio total.

Asiento
Guarda número, tipo y precio (obtenido desde PRECIOS_ASIENTO según el tipo).

Boleto
Código único, relación con la reserva y estado del boleto.

⚙️ Lógica y flujo de trabajo

El sistema obtiene los asientos asignados de la reserva.

Cada asiento es mostrado con:

Número

Tipo

Precio según PRECIOS_ASIENTO

Si es premium, económico, primera, etc., el valor se calcula automáticamente.

El email se genera como HTML y se envía usando configuración SMTP de Django.

🖥️ Frontend y experiencia del pasajero

Plantilla HTML optimizada para lectura en clientes de correo.

Tabla con los asientos asignados y precios.

Estilo claro, con secciones separadas para:

Datos del pasajero

Datos de la reserva

Datos del vuelo

Asientos y precios

Mensaje final de agradecimiento.

📦 Cómo poner en marcha este módulo

Configurar en settings.py las credenciales SMTP para envío de mails.

Crear la plantilla boleto_email.html dentro de templates/boletos/.

Definir el diccionario PRECIOS_ASIENTO con los precios por tipo.

Llamar a la función enviar_boleto_email(reserva) desde la vista que confirma la reserva.

Probar con python manage.py runserver y realizar una reserva para verificar el envío.

👨‍💻 Autor

Agustín Fasano
Estudiante de Desarrollo de Software en ITEC