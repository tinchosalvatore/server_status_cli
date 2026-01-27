# 🚀 CLI Uptime Monitor

Real-time website availability and latency monitoring tool, designed to run directly in the terminal. Built with **Python 3.10+**, it uses **AsyncIO** for high-performance concurrent checks and **Rich** for a modern visual interface.

## ✨ Features

* **Real-Time Monitoring:** Interactive dashboard that updates automatically (no infinite scroll).
* **High Performance:** Asynchronous engine (`asyncio` + `httpx`) capable of checking multiple sites simultaneously without blocking.
* **Visual Interface (TUI):** Tables with conditional formatting, status indicators (✅/❌), and colors based on latency.
* **Alerts:** Visual (intense red) and audible (system beep) feedback when a service goes down or returns an error (500, 404, DNS, etc.).
* **Persistent Management:** Lightweight JSON database to manage the list of clients and services without touching the code.

## 📂 Project Structure

```text
.
├── monitor.py        # Main monitoring script (Dashboard)
├── db.py             # CLI for database management (CRUD)
├── db.json           # Site database (automatically generated)
├── requirements.txt  # Project dependencies
├── setup.sh          # Automatic installation script
└── README.md         # Documentation

```

## 🛠️ Installation

The project includes an automated setup script for Unix/Linux/Mac environments.

1. **Clone the repository:**

```bash
git clone https://github.com/tinchosalvatore/server_status_cli.git
cd server_status_cli

```

2. **Run the setup:**
This script will create the virtual environment (`venv`) and install the necessary dependencies (`httpx`, `rich`).

```bash
chmod +x setup.sh
./setup.sh

```

3. **Activate the environment:**

```bash
source venv/bin/activate

```

## 🚀 Usage

The workflow is divided into two steps: configuration and monitoring.

### 1. 💾 Site Management (`db.py`)

Use this script to add, list, or remove the services you want to monitor.

```bash
python db.py

```

*Follow the on-screen instructions to add the client name, service, and URL.*

### 2. 📊 Start Monitor (`monitor.py`)

Once the sites are configured, launch the monitor. It will read the configuration and start the check cycle.

```bash
python monitor.py

```

* The dashboard will update every 10 seconds (configurable in the code).
* Press `Ctrl+C` to stop monitoring safely.

## ⚙️ Requirements

* Python 3.10 or higher.
* Internet connection.
* Terminal with color support (Standard ANSI/TrueColor).

## 📦 Main Libraries

* **[Rich](https://github.com/Textualize/rich):** For rendering tables, panels, and progress bars.
* **[HTTPX](https://github.com/encode/httpx):** Next-generation asynchronous HTTP client.

---

Made with 🖤 and Python.
