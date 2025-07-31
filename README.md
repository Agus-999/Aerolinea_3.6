🛫 Proyecto: Aerolínea Voladora
✨ Etapa 4: Empleados - Vuelos
En esta etapa desarrollamos la funcionalidad que permite a los empleados gestionar y visualizar los vuelos programados por la aerolínea.

1. 🧱 Modelado del modelo Vuelo
Creamos el modelo Vuelo con los siguientes campos:

✈️ Avión (avion)

🇦🇷 Origen (origen)

🇲🇽 Destino (destino)

📅 Fecha de salida (fecha_salida)

📅 Fecha de llegada (fecha_llegada)

🕓 Duración (duracion)

🚦 Estado (estado)

💵 Precio (precio)

2. 🧠 Lógica en la vista
Creamos la vista lista_vuelos en views.py para:

Consultar todos los vuelos.

Calcular automáticamente la duración (duracion = llegada - salida).

Mostrar los datos en español (fechas y duración traducidas).

3. 🧾 Plantilla lista.html
Creamos una plantilla tipo tabla que muestra los datos con el siguiente formato:

Avión	Origen	Destino	Salida	Llegada	Duración	Estado	Precio
Boeing 737	Argentina	México	1 de julio, 12:51	2 de julio, 12:52	1 día, 1 min	Programado	$150000.00

Se usó la función localize de Django y se habilitó el idioma español en settings.py.

4. 🌍 Traducción y localización
En el archivo settings.py, se ajustó la configuración regional:

python
Copiar
Editar
LANGUAGE_CODE = 'es'
USE_L10N = True
USE_I18N = True
USE_TZ = True
Además, en la plantilla se usó el filtro:

django
Copiar
Editar
{{ vuelo.fecha_salida|date:"j \\d\\e F \\a \\l\\a\\s H:i" }}
Para lograr una salida localizada, legible y completamente en español.

📁 Estructura actual del proyecto
Copiar
Editar
aerolinea_voladora/
├── aerolinea_voladora/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── empleados/
│   ├── models.py
│   ├── views.py
│   └── templates/
│       └── empleados/
│           └── lista.html
├── aerolineas_voladoras.sqlite3
├── manage.py
└── ...
✍️ Autor
Agustín Alejandro Fasano