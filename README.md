# ✈️ Sistema de Gestión de Reservas de Vuelos

Un sistema web desarrollado en **Django** para gestionar reservas de vuelos, con selección dinámica de asientos, edición y cancelación de reservas.  

---

## 🚀 Funcionalidades principales

- 👤 Gestión de reservas por usuario autenticado  
- 📝 Crear y editar reservas con datos completos del pasajero  
- 🪑 Selección visual e interactiva de hasta 4 asientos por reserva  
- 💳 Confirmación y bloqueo de asientos con actualización de estado y precio  
- 🗑️ Cancelación de reservas liberando los asientos ocupados  
- 📋 Listado y detalle de reservas con información completa  
- 🛫 **Creación automática de asientos** al registrar un nuevo avión  

---

## 📁 Estructura de archivos y carpetas

gestion/
├── migrations/
├── templates/
│ └── clientes/
│ └── reservas/
│ ├── detalle.html
│ ├── eliminar.html
│ ├── formulario.html
│ ├── lista.html
│ └── reserva.html
├── static/
│ └── (archivos estáticos: CSS, JS, imágenes)
├── forms.py
├── models.py
├── urls.py
├── views.py
└── tests.py

markdown
Copiar
Editar

---

## 🔗 URLs principales

| Ruta                             | Vista                 | Descripción                              |
|---------------------------------|-----------------------|------------------------------------------|
| `/mis-reservas/`                 | `mis_reservas`        | Lista de reservas del usuario            |
| `/reservas/crear/`               | `crear_reserva`       | Crear una nueva reserva                   |
| `/reservas/<reserva_id>/`        | `detalle_reserva`     | Ver detalle y editar datos de la reserva |
| `/reservas/<reserva_id>/editar/` | `editar_reserva`      | Editar datos del pasajero y vuelo        |
| `/reservas/<reserva_id>/eliminar/` | `eliminar_reserva`  | Cancelar reserva y liberar asientos      |
| `/reservas/<reserva_id>/asientos/` | `ver_asientos`      | Selección y visualización de asientos    |
| `/confirmar-compra/`             | `confirmar_compra`    | Confirmar compra y reservar asientos     |
| `/aviones/nuevo/`                | `nuevo_avion`         | Crear un nuevo avión con asientos automáticos |

---

## 🗃️ Modelos principales (`models.py`)

### Pasajero
- Datos personales y contacto
- Relación opcional con usuario autenticado

### Asiento
- Vinculado a un avión
- Número, fila, columna y tipo (`económico`, `premium`, `ejecutivo`, `primera`)
- Estado (`disponible` u `ocupado`)
- Precio asociado

### Reserva
- Relación con vuelo, pasajero y usuario
- Asientos reservados (ManyToMany)
- Estado (`pendiente`, `confirmada`, `cancelada`)
- Precio total y código único de reserva
- Métodos para liberar asientos y borrar reserva con seguridad

---

## 🆕 Cambios recientes

### ✈️ Creación automática de asientos al registrar un avión
Ahora, al crear un nuevo avión desde la vista `nuevo_avion`, el sistema genera automáticamente todos los asientos según las filas y columnas configuradas, asignando tipo de asiento en función de la fila:

- Filas 1-2 → Primera clase  
- Filas 3-6 → Ejecutivo  
- Filas 7-10 → Premium Economy  
- Filas restantes → Económico  

Además:
- El estado inicial de todos los asientos es **"disponible"**.
- Se valida que la cantidad de filas y columnas pueda cubrir la capacidad total del avión.

---

## ⚙️ Lógica y flujo de trabajo

- Autenticación obligatoria para todas las acciones de reserva  
- Validaciones de formulario para datos completos y correctos  
- En la selección de asientos, se bloquean los ya ocupados y máximo 4 por usuario  
- Confirmación de compra con transacciones para mantener integridad de datos  
- Liberación automática de asientos en edición o eliminación de reserva  
- **Generación automática de asientos** en la creación de un avión  

---

## 🖥️ Frontend y experiencia de usuario

- Interfaz responsive y amigable con Bootstrap  
- Grid visual para selección de asientos, con colores y precios destacados  
- Modal de confirmación con resumen claro de la compra  
- Alertas y mensajes para feedback inmediato al usuario  
- Navegación sencilla entre listado, detalle, edición y selección  

---

## 📦 Cómo poner en marcha el proyecto

1. Clonar el repositorio y configurar entorno virtual  
2. Instalar dependencias con `pip install -r requirements.txt`  
3. Ejecutar migraciones:  
   ```bash
   python manage.py migrate
Crear superusuario si se desea:

bash
Copiar
Editar
python manage.py createsuperuser
Levantar servidor local:

bash
Copiar
Editar
python manage.py runserver
Acceder en navegador a http://localhost:8000/mis-reservas/

👨‍💻 Autor
Agustín Fasano
Estudiante de Desarrollo de Software en ITEC