#!/bin/bash

# Server Status CLI Installer
# Author: Martin Salvatore

# --- Language Selector ---
echo "------------------------------------------------"
echo "Select Language / Seleccione Idioma"
echo "------------------------------------------------"
PS3="Choose/Elija (1-2): "
options=("English" "Español")
select opt in "${options[@]}"
do
    case $opt in
        "English")
            L_START="🚀 Starting Server Status CLI installation..."
            L_ERR_PY="❌ Error: Python 3 is not installed or not found."
            L_CLEAN="📦 Cleaning previous installations..."
            L_VENV="📦 Creating virtual environment in"
            L_DEPS="📥 Installing dependencies (Rich, HTTPX, Jinja2)..."
            L_LINK="🔗 Creating symlink in"
            L_SUCCESS="✅ Installation completed successfully!"
            L_TEST="Try your new tool:"
            L_TIP1="  $ sstatus          (Start real-time monitor)"
            L_TIP2="  $ sstatus -f -r    (Fast check and generate report)"
            L_TIP3="  $ sstatus-db       (Manage sites database)"
            L_PATH_NOTE="NOTE: Ensure this path is in your PATH:"
            LANG_CODE="en"
            break
            ;;
        "Español")
            L_START="🚀 Iniciando instalación de Server Status CLI..."
            L_ERR_PY="❌ Error: Python 3 no está instalado o no se encuentra."
            L_CLEAN="📦 Limpiando instalaciones previas..."
            L_VENV="📦 Creando entorno virtual en"
            L_DEPS="📥 Instalando librerías (Rich, HTTPX, Jinja2)..."
            L_LINK="🔗 Creando enlace simbólico en"
            L_SUCCESS="✅ ¡Instalación completada con éxito!"
            L_TEST="Prueba tu nueva tool:"
            L_TIP1="  $ sstatus          (Iniciar monitor en tiempo real)"
            L_TIP2="  $ sstatus -f -r    (Chequeo rápido y generar reporte)"
            L_TIP3="  $ sstatus-db       (Gestionar base de datos de sitios)"
            L_PATH_NOTE="NOTA: Asegúrate de que esta ruta está en tu PATH:"
            LANG_CODE="es"
            break
            ;;
        *) echo "Invalid option / Opción inválida $REPLY";;
    esac
done

APP_DIR="$HOME/.server_status_cli_app"
BIN_DIR="$HOME/.local/bin"
CONFIG_DIR="$HOME/.config/server-status-cli"
EXECUTABLE_NAME="sstatus"
DB_EXECUTABLE_NAME="sstatus-db"
PROJECT_DIR=$(pwd)

echo ""
echo "$L_START"

# 1. Verificar Python 3.10+
if ! command -v python3 &> /dev/null; then
    echo "$L_ERR_PY"
    exit 1
fi

# 2. Crear Entorno Virtual Limpio
echo "$L_CLEAN"
rm -rf "$APP_DIR"
echo "$L_VENV $APP_DIR..."
python3 -m venv "$APP_DIR"

# 3. Instalar Dependencias
echo "$L_DEPS"
"$APP_DIR/bin/pip" install -r requirements.txt --upgrade --quiet

# 4. Configurar Idioma en la nueva ruta XDG
mkdir -p "$CONFIG_DIR"
echo "{\"language\": \"$LANG_CODE\"}" > "$CONFIG_DIR/config.json"

# 5. Crear los Shims (Ejecutables) - Ya no necesitan cd porque el código usa rutas absolutas
echo "$L_LINK $BIN_DIR..."
mkdir -p "$BIN_DIR"

# Shim para el monitor
cat > "$BIN_DIR/$EXECUTABLE_NAME" <<EOF
#!/bin/bash
"$APP_DIR/bin/python" "$PROJECT_DIR/monitor.py" "\$@"
EOF

# Shim para la base de datos
cat > "$BIN_DIR/$DB_EXECUTABLE_NAME" <<EOF
#!/bin/bash
"$APP_DIR/bin/python" "$PROJECT_DIR/db.py" "\$@"
EOF

chmod +x "$BIN_DIR/$EXECUTABLE_NAME"
chmod +x "$BIN_DIR/$DB_EXECUTABLE_NAME"

# 6. Finalización
echo ""
echo "$L_SUCCESS"
echo "------------------------------------------------"
echo "$L_TEST"
echo "$L_TIP1"
echo "$L_TIP2"
echo "$L_TIP3"
echo "------------------------------------------------"
echo "$L_PATH_NOTE $BIN_DIR"
