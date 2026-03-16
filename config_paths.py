import os
from platformdirs import user_config_dir, user_downloads_dir

# Rutas de la Aplicación
APP_NAME = "server-status-cli"

# Carpeta de configuración (donde vive db.json y config.json)
# En Linux: ~/.config/server-status-cli
CONFIG_DIR = user_config_dir(APP_NAME)

# Carpeta de Reportes por defecto: La carpeta de descargas del usuario
# platformdirs detecta automáticamente si es "Downloads", "Descargas", etc.
REPORTS_DIR = user_downloads_dir()

# Archivos específicos
DB_FILE = os.path.join(CONFIG_DIR, "db.json")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def ensure_dirs():
    """Asegura que los directorios necesarios existan."""
    os.makedirs(CONFIG_DIR, exist_ok=True)
    # No creamos la de descargas porque ya debería existir en el OS

# Ruta base del código para encontrar plantillas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
