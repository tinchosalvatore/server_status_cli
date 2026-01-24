# 🚀 CLI Uptime Monitor

Herramienta de monitoreo de disponibilidad y latencia de sitios web en tiempo real, diseñada para ejecutarse directamente en la terminal. Construida con **Python 3.10+**, utiliza **AsyncIO** para chequeos concurrentes de alto rendimiento y **Rich** para una interfaz visual moderna.

![Python Version](https://img.shields.io/badge/python-3.10-blue)

![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Características

* **Monitoreo en Tiempo Real:** Dashboard interactivo que se actualiza automáticamente (sin scroll infinito).
* **Alto Rendimiento:** Motor asíncrono (`asyncio` + `httpx`) capaz de chequear múltiples sitios simultáneamente sin bloqueos.
* **Interfaz Visual (TUI):** Tablas con formato condicional, indicadores de estado (✅/❌) y colores según latencia.
* **Alertas:** Feedback visual (rojo intenso) y sonoro (system beep) cuando un servicio cae o devuelve un error (500, 404, DNS, etc.).
* **Gestión Persistente:** Base de datos ligera en JSON para administrar la lista de clientes y servicios sin tocar el código.

## 📂 Estructura del Proyecto

```text
.
├── monitor.py        # Script principal de monitoreo (Dashboard)
├── db.py             # CLI para gestión de la base de datos (CRUD)
├── db.json           # Base de datos de sitios (generada automáticamente)
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
Este script creará el entorno virtual (`venv`) e instalará las dependencias necesarias (`httpx`, `rich`).
```bash
chmod +x setup.sh
./setup.sh

```


3. **Activar el entorno:**
```bash
source venv/bin/activate

```

## 🚀 Uso

El flujo de trabajo se divide en dos pasos: configuración y monitoreo.

### 1. 💾 Gestión de Sitios (`db.py`)

Utiliza este script para agregar, listar o eliminar los servicios que deseas monitorear.

```bash
python db.py

```

*Sigue las instrucciones en pantalla para añadir el nombre del cliente, el servicio y la URL.*

### 2. 📊 Iniciar Monitor (`monitor.py`)

Una vez configurados los sitios, lanza el monitor. Este leerá la configuración y comenzará el ciclo de chequeos.

```bash
python monitor.py
```

* El dashboard se actualizará cada 10 segundos (configurable en el código).
* Presiona `Ctrl+C` para detener el monitoreo de forma segura.

## ⚙️ Requisitos

* Python 3.10 o superior.
* Conexión a internet.
* Terminal con soporte de colores (Standard ANSI/TrueColor).

## 📦 Librerías Principales

* **[Rich](https://github.com/Textualize/rich):** Para el renderizado de tablas, paneles y barras de progreso.
* **[HTTPX](https://github.com/encode/httpx):** Cliente HTTP asíncrono de próxima generación.

---

Hecho con 🖤 y Python.