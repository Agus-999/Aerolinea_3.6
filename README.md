🛫 Proyecto: Aerolínea Voladora
✨ Etapa 5: Clientes - Visualización de Vuelos
En esta etapa desarrollamos la funcionalidad destinada a los clientes, permitiéndoles visualizar de forma clara, atractiva y accesible los vuelos disponibles junto con los datos del avión.

1. 🧱 Combinación de datos de vuelo y avión
Creamos una vista que combina la información del vuelo con la del avión para facilitar la comprensión al cliente:

✈️ Modelo del avión

🪑 Capacidad

⚙️ Fabricante

🛫 Origen del vuelo

🛬 Destino

📅 Fecha y hora de salida/llegada

🕓 Duración calculada

💵 Precio

🚦 Estado del vuelo

2. 🎨 Diseño de tarjeta visual (template lista_clientes.html)
En lugar de una tabla, diseñamos tarjetas individuales estilo "cajas" para mostrar los vuelos:

En la parte superior: imagen representativa del avión.

Debajo: información del vuelo y del avión en una estructura tipo tarjeta.

Estilo responsive y moderno con bordes, colores y espaciado.

3. 📄 Página de detalle (detalle.html)
Creamos una página donde el cliente puede hacer clic en un vuelo y ver sus detalles ampliados:

Se reutiliza el diseño visual atractivo.

Se muestran todos los datos del avión y del vuelo.

Se permite volver fácilmente a la lista general de vuelos.

4. 🌍 Localización en español
Continuamos usando localización en español para mostrar fechas y horas de forma natural:

django
Copiar código
{{ vuelo.fecha_salida|date:"j \\d\\e F \\a \\l\\a\\s H:i" }}
Además, en settings.py se mantiene:

python
Copiar código
LANGUAGE_CODE = 'es'
USE_L10N = True
USE_I18N = True
USE_TZ = True
📁 Estructura del proyecto (resumen relevante)

Copiar código
aerolinea_voladora/
├── aerolinea_voladora/
│   └── settings.py
├── empleados/
│   └── models.py
├── clientes/
│   ├── views.py
│   └── templates/
│       └── clientes/
│           ├── lista_clientes.html
│           └── detalle.html
✍️ Autor:
Agustín Alejandro Fasano