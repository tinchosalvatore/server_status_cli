import json
import os
from config_paths import CONFIG_FILE

STRINGS = {
    "es": {
        "monitor_title": "UPTIME MONITOR",
        "monitor_status": "UPTIME STATUS",
        "starting_monitor": "Iniciando monitor en tiempo real... (Ctrl+C para salir)",
        "next_update": "Próxima actualización en",
        "error_db_not_found": "Error: No se encontró db.json. Ejecuta db.py primero.",
        "checking_once": "Ejecutando un único chequeo...",
        "report_success": "✔ Reporte generado exitosamente en:",
        "unexpected_error": "Ha ocurrido un error inesperado:",
        "stop_monitor": "Monitor detenido correctamente.",
        "col_client": "Cliente",
        "col_service": "Servicio",
        "col_status": "Status",
        "col_code": "Code",
        "col_latency": "Latencia",
        "db_manager_title": "🔧 Monitor Manager v1.2",
        "db_empty": "La base de datos está vacía.",
        "db_table_title": "Sitios Configurados",
        "db_add_title": "Agregar Nuevo Sitio",
        "db_prompt_client": "👤 Nombre del Cliente",
        "db_prompt_service": "🏷️  Nombre del Servicio (ej. Landing, API)",
        "db_prompt_url": "🔗 URL del sitio",
        "db_url_error": "La URL debe comenzar con http:// o https://",
        "db_add_success": "¡Sitio agregado exitosamente!",
        "db_delete_title": "Eliminar Sitio",
        "db_delete_prompt": "Ingresa el [cyan]ID[/] del sitio a borrar (o 'c' para cancelar)",
        "db_delete_success": "🗑️ Sitio eliminado:",
        "db_invalid_id": "❌ ID inválido.",
        "db_invalid_number": "❌ Debes ingresar un número.",
        "db_no_sites_delete": "No hay sitios para eliminar.",
        "db_menu_option": "Selecciona una opción",
        "db_menu_1": "Agregar sitio",
        "db_menu_2": "Listar sitios",
        "db_menu_3": "Eliminar sitio",
        "db_menu_4": "Salir",
        "db_bye": "¡Hasta luego!",
        "db_read_error": "⚠ Error al leer el archivo JSON. Se iniciará una lista vacía.",
        "db_save_success": "✔ Base de datos guardada en",
        "report_title": "Reporte de Disponibilidad",
        "report_subtitle": "Estado de servicios monitoreados",
        "report_summary": "Resumen",
        "report_total": "Total Servicios",
        "report_up": "En línea",
        "report_down": "Caídos",
        "report_generated_at": "Generado el",
        "report_col_url": "URL",
        "report_status_online": "ONLINE",
        "report_status_offline": "OFFLINE"
    },
    "en": {
        "monitor_title": "UPTIME MONITOR",
        "monitor_status": "UPTIME STATUS",
        "starting_monitor": "Starting real-time monitor... (Ctrl+C to exit)",
        "next_update": "Next update in",
        "error_db_not_found": "Error: db.json not found. Run db.py first.",
        "checking_once": "Running a single check...",
        "report_success": "✔ Report successfully generated at:",
        "unexpected_error": "An unexpected error occurred:",
        "stop_monitor": "Monitor stopped correctly.",
        "col_client": "Client",
        "col_service": "Service",
        "col_status": "Status",
        "col_code": "Code",
        "col_latency": "Latency",
        "db_manager_title": "🔧 Monitor Manager v1.2",
        "db_empty": "Database is empty.",
        "db_table_title": "Configured Sites",
        "db_add_title": "Add New Site",
        "db_prompt_client": "👤 Client Name",
        "db_prompt_service": "🏷️  Service Name (e.g. Landing, API)",
        "db_prompt_url": "🔗 Site URL",
        "db_url_error": "URL must start with http:// or https://",
        "db_add_success": "Site added successfully!",
        "db_delete_title": "Delete Site",
        "db_delete_prompt": "Enter the site [cyan]ID[/] to delete (or 'c' to cancel)",
        "db_delete_success": "🗑️ Site deleted:",
        "db_invalid_id": "❌ Invalid ID.",
        "db_invalid_number": "❌ You must enter a number.",
        "db_no_sites_delete": "No sites to delete.",
        "db_menu_option": "Select an option",
        "db_menu_1": "Add site",
        "db_menu_2": "List sites",
        "db_menu_3": "Delete site",
        "db_menu_4": "Exit",
        "db_bye": "Goodbye!",
        "db_read_error": "⚠ Error reading JSON file. Starting with an empty list.",
        "db_save_success": "✔ Database saved in",
        "report_title": "Availability Report",
        "report_subtitle": "Status of monitored services",
        "report_summary": "Summary",
        "report_total": "Total Services",
        "report_up": "Online",
        "report_down": "Down",
        "report_generated_at": "Generated at",
        "report_col_url": "URL",
        "report_status_online": "ONLINE",
        "report_status_offline": "OFFLINE"
    }
}

def get_language():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                return config.get("language", "en")
        except:
            return "en"
    return "en"

def _(key):
    lang = get_language()
    return STRINGS.get(lang, STRINGS["en"]).get(key, key)

def get_all_strings():
    lang = get_language()
    return STRINGS.get(lang, STRINGS["en"])