🎫 Gestión de Boletos – Módulo para Empleados

Un módulo del sistema de gestión de vuelos desarrollado en Django, que permite a los empleados ver, listar y verificar boletos de los pasajeros de manera rápida y segura.

🚀 Funcionalidades principales

📋 Lista completa de boletos con información detallada:

Código de barra

Nombre del pasajero

Documento

Vuelo

Fecha de salida

Precio

Estado del boleto

🔍 Verificación de boletos: los empleados pueden verificar si un boleto es válido y cambiar su estado de “emitido” a “verificado” o “confirmado”.

🎨 Diseño moderno tipo “ticket” con colores según el estado.

🔒 Acceso exclusivo para empleados autenticados.

🖥️ Interfaz responsive y clara, optimizada para desktops y tablets.

📁 Estructura de archivos y carpetas
gestion/
├── migrations/
├── templates/
│   └── empleados/
│       └── boletos/
│           ├── lista_boletos.html
│           └── verificar_boleto.html
├── static/
│   └── (CSS, JS, imágenes, etc.)
├── forms.py
├── models.py
├── urls.py
├── views.py
└── tests.py

🔗 URLs principales
Ruta	Vista	Descripción
/gestion/empleados/boletos/	lista_boletos_empleado	Lista todos los boletos disponibles
/gestion/empleados/boletos/verificar/<codigo>/	verificar_boleto_empleado	Verifica un boleto específico y cambia su estado
🗃️ Modelo principal (models.py)

Boleto

reserva → relación con la reserva del pasajero

codigo_barra → código único del boleto

estado → emitido, verificado, etc.

Método __str__() para mostrar el código de manera legible

Reserva

Información del pasajero, vuelo, asientos y precio

Estado de la reserva

⚙️ Lógica y flujo de trabajo

Los empleados deben estar autenticados para acceder al módulo.

Los boletos se listan en cards visuales tipo ticket para mejorar la experiencia.

Al verificar un boleto:

Se valida que esté emitido y la reserva esté confirmada.

El estado del boleto se actualiza a verificado.

Todas las operaciones tienen feedback visual mediante alertas o cambios de color según estado.

🖥️ Frontend y experiencia de usuario

Diseño moderno con Bootstrap y estilos tipo ticket.

Colores y badges para diferenciar estados de boletos.

Botón Verificar en cada boleto para un acceso rápido.

Lista responsive que se ajusta a diferentes tamaños de pantalla.

📦 Cómo poner en marcha este módulo

Asegurarse de tener el proyecto principal clonado y virtualenv activado.

Ejecutar migraciones si hay cambios en Boleto o Reserva:

python manage.py makemigrations gestion
python manage.py migrate


Levantar servidor local:

python manage.py runserver


Acceder a: http://localhost:8000/gestion/empleados/boletos/ para ver la lista de boletos.

👨‍💻 Autor

Agustín Fasano
Estudiante de Desarrollo de Software en ITEC