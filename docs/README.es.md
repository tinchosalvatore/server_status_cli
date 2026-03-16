# 🚀 CLI Uptime Monitor

*Read in [English](README.md).*

Herramienta de monitoreo de disponibilidad y latencia de sitios web en tiempo real, diseñada para ejecutarse directamente en la terminal. Construida con **Python 3.10+**, utiliza **AsyncIO** para chequeos concurrentes de alto rendimiento y **Rich** para una interfaz visual moderna.

## ✨ Características

* **Monitoreo en Tiempo Real:** Dashboard interactivo que se actualiza automáticamente (sin scroll infinito).
* **Alto Rendimiento:** Motor asíncrono (`asyncio` + `httpx`) capaz de chequear múltiples sitios simultáneamente sin bloqueos.
* **Interfaz Visual (TUI):** Tablas con formato condicional, indicadores de estado (✅/❌) y colores según latencia.
* **Alertas:** Feedback visual (rojo intenso) y sonoro (system beep) cuando un servicio cae o devuelve un error (500, 404, DNS, etc.).
* **Gestión Persistente:** Base de datos ligera en JSON para administrar la lista de clientes y servicios sin tocar el código.
* **Reportes en HTML:** Genera un reporte HTML profesional con temática oscura que incluye los resultados de los chequeos, guardado en el directorio `reports`.

---
## 📂 Estructura del Proyecto

```text
.
├── monitor.py        # Script principal de monitoreo (Dashboard)
├── db.py             # CLI para gestión de la base de datos (CRUD)
├── report.py         # Lógica para generar reportes
├── db.json           # Base de datos de sitios
├── templates/        # Plantillas HTML y CSS para los reportes
├── reports/          # Directorio donde se guardan los reportes
├── requirements.txt  # Dependencias del proyecto
├── setup.sh          # Script de instalación automática
└── README.md         # Documentación
```

## 🛠️ Instalación

El proyecto incluye un script de configuración automatizado para entornos Unix/Linux/Mac.

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tinchosalvatore/server_status_cli.git
cd server_status_cli
```

2. **Ejecutar el setup:**
Este script creará el entorno virtual (`venv`) e instalará las dependencias necesarias (`httpx`, `rich`, `jinja2`).
```bash
chmod +x setup.sh
./setup.sh
```

3. **Activar el entorno:**
```bash
source venv/bin/activate
```

---
## 🚀 Uso

El flujo de trabajo se divide en dos pasos: configuración y monitoreo.

### 1. 💾 Gestión de Sitios (`db.py`)

Utiliza este script para agregar, listar o eliminar los servicios que deseas monitorear.

```bash
python db.py
```

*Sigue las instrucciones en pantalla para añadir el nombre del cliente, el servicio y la URL.*

### 2. 📊 Iniciar Monitor (`monitor.py`)

Una vez configurados los sitios, lanza el monitor.

*   **Para monitoreo en tiempo real:**
    ```bash
    python monitor.py
    ```
    * El dashboard se actualizará cada 10 segundos (configurable).
    * Presiona `Ctrl+C` para detenerlo.

*   **Monitoreo único instantáneo:**
    ```bash
    python monitor.py -f
    # o
    python monitor.py --fast
    ```
    * Este comando ejecuta un único chequeo, sin consumir toda la terminal.

*   **Para generar un reporte en HTML:**
    ```bash
    python monitor.py -r
    # o
    python monitor.py --report
    ```
    * Este comando ejecuta un único chequeo y guarda un reporte HTML detallado con estilos CSS en el directorio `reports/`.

*   **Siéntete libre de combinar ambos comandos:**
    ```bash
    python monitor.py -f -r
    # o
    python monitor.py --fast --report
    ```
    * Esta es la forma más eficiente de chequear múltiples sitios a la vez y obtener una salida visualmente atractiva.

---
## ⚙️ Requisitos

* Python 3.10 o superior.
* Conexión a internet.
* Terminal con soporte de colores (Standard ANSI/TrueColor).

## 📦 Librerías Principales

* **[Rich](https://github.com/Textualize/rich):** Para el renderizado de tablas, paneles y barras de progreso.
* **[HTTPX](https://github.com/encode/httpx):** Cliente HTTP asíncrono de próxima generación.
* **[Jinja2](https://jinja.palletsprojects.com/):** Para el renderizado de plantillas HTML.

---

Hecho con 🖤 y Python por [Martin Salvatore](https://github.com/tinchosalvatore).
