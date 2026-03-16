# 🚀 CLI Uptime Monitor

*Leer en [Español](README.es.md).*

Real-time website availability and latency monitoring tool, designed to run directly in the terminal. Built with **Python 3.10+**, it uses **AsyncIO** for high-performance concurrent checks and **Rich** for a modern visual interface.

## ✨ Features

* **Real-Time Monitoring:** Interactive dashboard that updates automatically.
* **Multi-language Support:** Fully localized in English and Spanish.
* **Global Commands:** Run the tool from anywhere using `sstatus`.
* **High Performance:** Asynchronous engine (`asyncio` + `httpx`) capable of checking multiple sites simultaneously.
* **Visual Interface (TUI):** Tables with conditional formatting and latency-based colors.
* **Alerts:** Visual and audible feedback (system beep) on service failures.
* **HTML Reports:** Professional dark-themed reports with custom output directory support.

---
## 📂 Project Structure

```text
.
├── config_paths.py   # Global path management (XDG standard)
├── monitor.py        # Main monitoring script
├── db.py             # Database management CLI
├── i18n.py           # Internationalization engine
├── report.py         # Report generation logic
├── templates/        # HTML/CSS templates for reports
├── setup.sh          # Interactive installer
└── uninstall.sh      # Interactive uninstaller
```

## 🛠️ Installation

The project includes an interactive setup script that configures a virtual environment and creates global commands.

1. **Clone the repository:**
```bash
git clone https://github.com/tinchosalvatore/server_status_cli.git
cd server_status_cli
```

2. **Run the setup:**
Choose your preferred language during the process.
```bash
chmod +x setup.sh
./setup.sh
```

*Note: The script creates shims in `~/.local/bin`. Make sure this directory is in your `PATH`.*

---
## 🚀 Usage

### 1. 💾 Site Management
Use the database manager to add or remove services.
```bash
sstatus-db
```

### 2. 📊 Start Monitor
Launch the real-time dashboard:
```bash
sstatus
```

*   **Fast check (single run):**
    ```bash
    sstatus -f
    ```
*   **Generate HTML Report:**
    ```bash
    sstatus -r
    ```
*   **Custom Report Output:**
    Specify where to save the HTML report.
    ```bash
    sstatus -r -o /path/to/my_reports
    ```

### ⚙️ Configuration & Data
The app follows standard OS conventions to keep your home directory clean:
- **Database (`db.json`):** Located in your user config directory (e.g., `~/.config/server-status-cli/`).
- **Settings (`config.json`):** Same as the database.
- **Default Reports:** Your system's **Downloads** folder (detected automatically by OS).

*This ensures your data persists even if you move or update the project folder.*

---
## 🗑️ Uninstallation

To completely remove the application and its environment:
```bash
chmod +x uninstall.sh
./uninstall.sh
```
*The script will ask if you want to keep or delete your site database and configuration.*

---
## ⚙️ Requirements

* Python 3.10 or higher.
* Terminal with color support (Standard ANSI/TrueColor).

## 📦 Main Libraries

* **[Rich](https://github.com/Textualize/rich):** TUI rendering.
* **[HTTPX](https://github.com/encode/httpx):** Asynchronous HTTP client.
* **[Jinja2](https://jinja.palletsprojects.com/):** HTML templates.

---

Made with 🖤 and Python by [Martin Salvatore](https://github.com/tinchosalvatore).
