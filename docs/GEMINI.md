# 🧠 Proyecto: CLI Uptime Monitor (Contexto para Gemini)

Este archivo sirve como base de conocimiento para Gemini CLI sobre la estructura, arquitectura y lógica del proyecto **Server Status CLI**.

## 📋 Resumen del Proyecto
Herramienta de monitoreo de disponibilidad y latencia de sitios web en tiempo real, diseñada para la terminal. Utiliza Python asíncrono para chequeos concurrentes y una interfaz visual moderna (TUI).

## 🏗️ Arquitectura y Componentes Clave

### 1. Monitoreo (`monitor.py`)
- **Motor:** `httpx.AsyncClient` + `asyncio` para peticiones concurrentes.
- **Interfaz:** `rich.live` y `rich.table` para un dashboard interactivo que se refresca cada 10s.
- **Modos de Ejecución:**
  - `python monitor.py`: Dashboard en tiempo real (loop infinito).
  - `python monitor.py -f`: Chequeo rápido único (Fast check).
  - `python monitor.py -r`: Generación de reporte HTML único.
- **Lógica de Éxito:** Se considera exitoso si el `status_code == 200`.

### 2. Gestión de Datos (`db.py` y `db.json`)
- **Persistencia:** Archivo `db.json` que almacena una lista de diccionarios con `client`, `name` y `url`.
- **CRUD:** `db.py` es una CLI interactiva para gestionar los sitios sin editar el JSON manualmente.

### 3. Reportes (`report.py`)
- **Motor de Plantillas:** `Jinja2`.
- **Recursos:** Utiliza `templates/report_template.html` y `templates/style.css`.
- **Salida:** Genera archivos `.html` en el directorio `reports/` con marcas de tiempo.

## 🛠️ Stack Tecnológico
- **Python 3.10+**
- **HTTPX:** Peticiones HTTP asíncronas.
- **Rich:** Formateo de tablas, colores y paneles en terminal.
- **Jinja2:** Renderizado de reportes HTML.

## 📂 Estructura de Archivos Críticos
- `monitor.py`: Lógica principal y TUI.
- `db.py`: Gestor de la base de datos JSON.
- `report.py`: Generador de reportes.
- `db.json`: Almacenamiento de sitios (creado tras usar `db.py`).
- `templates/`: Plantillas para el reporte HTML.
- `reports/`: Directorio de salida de reportes (ignorado por Git normalmente).

## 💡 Notas para Desarrollo Futuro
- **Alertas:** El monitor emite un "system beep" (`\a`) cuando detecta un fallo.
- **Latencia:** Los umbrales de color son: Verde (<500ms), Amarillo (500ms-1000ms), Rojo (>1000ms).
- **Extensiones:** Al añadir campos en `db.json`, asegúrate de actualizar la dataclass `CheckResult` en `monitor.py` y la lógica de renderizado en `report.py`.

## 🚀 Comandos Comunes
- Instalar: `./setup.sh`
- Agregar sitio: `python db.py` (Opción 1)
- Iniciar monitor: `python monitor.py`
- Reporte rápido: `python monitor.py -f -r`
