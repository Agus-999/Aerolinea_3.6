# ✈️ Proyecto Django: Aerolíneas Voladoras

## 🛫 Etapa 1: Creación del proyecto y conexión con base de datos

---

### 1. 🧱 Creación del entorno virtual
Creamos y activamos un entorno virtual para aislar dependencias del proyecto:

    python -m venv venv
    venv\Scripts\activate  # En Windows


### 2. ⚙️ Instalación de Django
Instalamos Django dentro del entorno virtual:

    pip install django

### 3. 📁 Creación del proyecto base
Creamos el proyecto Django en la raíz actual (evitando guiones, que pueden causar problemas en Python):

    django-admin startproject aerolinea_voladora .

### 4. 🗄️ Conexión con la base de datos existente
Ya contábamos con una base de datos SQLite llamada:

    aerolineas_voladoras.sqlite3

### ✅ La colocamos en la raíz del proyecto, junto a manage.py.

### 🔧 Luego, editamos settings.py para usarla:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "aerolineas_voladoras.sqlite3",
    }
}

### 5. ✅ Verificación del proyecto
Aplicamos las migraciones iniciales de Django para asegurarnos de que todo está bien conectado:

### 📁 Estructura actual del proyecto

aerolinea_voladora/
├── aerolinea_voladora/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── aerolineas_voladoras.sqlite3
├── manage.py
├── requirements.txt  # (Podés generarlo luego con `pip freeze > requirements.txt`)
└── venv/

### ✍️ Autor
    Agustín Alejandro Fasano
