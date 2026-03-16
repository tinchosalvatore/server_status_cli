# 🚀 CLI Uptime Monitor

*Read in [English](README.md).*

Herramienta de monitoreo de disponibilidad y latencia de sitios web en tiempo real, diseñada para ejecutarse directamente en la terminal. Construida con **Python 3.10+**, utiliza **AsyncIO** para chequeos concurrentes de alto rendimiento y **Rich** para una interfaz visual moderna.

## ✨ Características

* **Monitoreo en Tiempo Real:** Dashboard interactivo que se actualiza automáticamente.
* **Soporte Multi-lenguaje:** Totalmente localizado en Inglés y Español.
* **Comandos Globales:** Ejecuta la herramienta desde cualquier parte usando `sstatus`.
* **Alto Rendimiento:** Motor asíncrono (`asyncio` + `httpx`) capaz de chequear múltiples sitios simultáneamente.
* **Interfaz Visual (TUI):** Tablas con formato condicional y colores basados en latencia.
* **Alertas:** Feedback visual y sonoro (system beep) ante fallos en los servicios.
* **Reportes HTML:** Reportes profesionales con tema oscuro y soporte para directorio de salida personalizado.

---
## 📂 Estructura del Proyecto

```text
.
├── config_paths.py   # Gestión global de rutas (XDG standard)
├── monitor.py        # Script principal de monitoreo
├── db.py             # CLI de gestión de base de datos
├── i18n.py           # Motor de internacionalización
├── report.py         # Lógica de generación de reportes
├── templates/        # Plantillas HTML/CSS para reportes
├── setup.sh          # Instalador interactivo
└── uninstall.sh      # Desinstalador interactivo
```


## 🛠️ Instalación

El proyecto incluye un script de configuración interactivo que configura un entorno virtual y crea comandos globales.

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tinchosalvatore/server_status_cli.git
cd server_status_cli
```

2. **Ejecutar el setup:**
Elige tu idioma preferido durante el proceso.
```bash
chmod +x setup.sh
./setup.sh
```

*Nota: El script crea accesos directos en `~/.local/bin`. Asegúrate de que este directorio esté en tu `PATH`.*

---
## 🚀 Uso

### 1. 💾 Gestión de Sitios
Usa el gestor de base de datos para añadir o eliminar servicios.
```bash
sstatus-db
```

### 2. 📊 Iniciar Monitor
Lanza el dashboard en tiempo real:
```bash
sstatus
```

*   **Chequeo rápido (ejecución única):**
    ```bash
    sstatus -f
    ```
*   **Generar Reporte HTML:**
    ```bash
    sstatus -r
    ```
*   **Directorio de Reportes Personalizado:**
    Especifica dónde guardar el reporte HTML.
    ```bash
    sstatus -r -o /ruta/a/mis_reportes
    ```

### ⚙️ Configuración y Datos
La aplicación sigue las convenciones del sistema operativo para mantener tu carpeta personal limpia:
- **Base de Datos (`db.json`):** Ubicada en tu directorio de configuración de usuario (ej. `~/.config/server-status-cli/`).
- **Ajustes (`config.json`):** Igual que la base de datos.
- **Reportes por Defecto:** La carpeta **Descargas** de tu sistema (detectada automáticamente por el SO).

*Esto asegura que tus datos persistan incluso si mueves o actualizas la carpeta del proyecto.*


---
## 🗑️ Desinstalación

Para eliminar completamente la aplicación y su entorno:
```bash
chmod +x uninstall.sh
./uninstall.sh
```
*El script preguntará si quieres mantener o borrar tu base de datos de sitios y configuración.*

---
## ⚙️ Requisitos

* Python 3.10 o superior.
* Terminal con soporte de colores (Standard ANSI/TrueColor).

## 📦 Librerías Principales

* **[Rich](https://github.com/Textualize/rich):** Renderizado de TUI.
* **[HTTPX](https://github.com/encode/httpx):** Cliente HTTP asíncrono.
* **[Jinja2](https://jinja.palletsprojects.com/):** Plantillas HTML.

---

Hecho con 🖤 y Python por [Martin Salvatore](https://github.com/tinchosalvatore).
