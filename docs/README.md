# 🚀 CLI Uptime Monitor

*Leer en [Español](README.es.md).*

Real-time website availability and latency monitoring tool, designed to run directly in the terminal. Built with **Python 3.10+**, it uses **AsyncIO** for high-performance concurrent checks and **Rich** for a modern visual interface.

## ✨ Features

* **Real-Time Monitoring:** Interactive dashboard that updates automatically (no infinite scroll).
* **High Performance:** Asynchronous engine (`asyncio` + `httpx`) capable of checking multiple sites simultaneously without blocking.
* **Visual Interface (TUI):** Tables with conditional formatting, status indicators (✅/❌), and colors based on latency.
* **Alerts:** Visual (intense red) and audible (system beep) feedback when a service goes down or returns an error (500, 404, DNS, etc.).
* **Persistent Management:** Lightweight JSON database to manage the list of clients and services without touching the code.
* **HTML Reports:** Generates a professional, dark-themed HTML report with the check results, saved in the `reports` directory.

---
## 📂 Project Structure

```text
.
├── monitor.py        # Main monitoring script (Dashboard)
├── db.py             # CLI for database management (CRUD)
├── report.py         # Report generation logic
├── db.json           # Site database
├── templates/        # HTML and CSS templates for reports
├── reports/          # Directory where reports are saved
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
This script will create the virtual environment (`venv`) and install the necessary dependencies (`httpx`, `rich`, `jinja2`).

```bash
chmod +x setup.sh
./setup.sh

```

3. **Activate the environment:**

```bash
source venv/bin/activate

```

---
## 🚀 Usage

The workflow is divided into two steps: configuration and monitoring.

### 1. 💾 Site Management (`db.py`)

Use this script to add, list, or remove the services you want to monitor.

```bash
python db.py

```

*Follow the on-screen instructions to add the client name, service, and URL.*

### 2. 📊 Start Monitor (`monitor.py`)

Once the sites are configured, launch the monitor.

*   **For real-time monitoring:**
    ```bash
    python monitor.py
    ```
    * The dashboard will update every 10 seconds (configurable).
    * Press `Ctrl+C` to stop.

*   **Instant unique monitoring:**
    ```bash
    python monitor.py -f
    # or
    python monitor.py --fast
    ```
    * This command runs a single check, without consuming the hole terminal use.

*   **To generate an HTML report:**
    ```bash
    python monitor.py -r
    # or
    python monitor.py --report
    ```
    * This command runs a single check and saves a detailed HTML with CSS style report in the `reports/` directory.

*   **Feel free to combine the two commands**
    ```bash
    python monitor.py -f -r
    # or
    python monitor.py --fast --report
    ```
    * For me this is the most efficient way to check multiple sites at once and have the good looking output.

---
## ⚙️ Requirements

* Python 3.10 or higher.
* Internet connection.
* Terminal with color support (Standard ANSI/TrueColor).

## 📦 Main Libraries

* **[Rich](https://github.com/Textualize/rich):** For rendering tables, panels, and progress bars.
* **[HTTPX](https://github.com/encode/httpx):** Next-generation asynchronous HTTP client.
* **[Jinja2](https://jinja.palletsprojects.com/):** For HTML template rendering.

---

Made with 🖤 and Python by [Martin Salvatore](https://github.com/tinchosalvatore).