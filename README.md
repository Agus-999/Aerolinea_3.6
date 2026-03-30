# 🛫 Sistema de Gestión de Vuelos y Reservas (Django)

Este proyecto es una plataforma integral de gestión aerolínea desarrollada en **Django**, enfocada en la administración eficiente de vuelos, pasajeros y asignación de asientos en tiempo real.

### 🚀 Funcionalidades Principales

* **Panel de Gestión de Reservas:** Visualización detallada de estados de vuelos, origen/destino y datos de pasajeros.
* **Gestión Inteligente de Asientos:** Sistema dinámico que identifica reservas sin asignación y permite el seguimiento de disponibilidad.
* **Filtros Avanzados:** Motor de búsqueda optimizado para localizar reservas por vuelo, pasajero o estado del documento.
* **Lógica de Negocio Robusta:** Implementación de relaciones *Many-to-Many* para la gestión de asientos y validación de duplicados.

### 🛠️ Stack Tecnológico
* **Backend:** Python 3.x & Django Framework.
* **Base de Datos:** SQLite / PostgreSQL (Relacional).
* **Frontend:** HTML5, CSS3 con lógica de plantillas dinámicas de Django.
* **Optimización:** Uso de `select_related` y `prefetch_related` para reducir la carga en la base de datos y mejorar la performance.

### 📁 Arquitectura del Módulo de Gestión
El sistema sigue el patrón **MVT (Model-View-Template)**, con una estructura organizada para escalabilidad:
* `models.py`: Definición de entidades complejas (Reserva, Vuelo, Asiento).
* `views.py`: Lógica de procesamiento de reportes y filtros dinámicos.
* `templates/`: Interfaces optimizadas para la experiencia del usuario administrativo.

### ⚙️ Desafíos Técnicos Resueltos
* **Optimización de Consultas:** Implementación de `.distinct()` y precarga de datos para evitar el problema de consultas N+1 en relaciones ManyToMany.
* **UX Administrativa:** Diseño de una interfaz clara para que el personal pueda detectar rápidamente reservas pendientes de asignación.

---
**Desarrollado por [Agustín Alejandro Fasano](https://github.com/Agus-999)** *Técnico Superior en Desarrollo de Software*
