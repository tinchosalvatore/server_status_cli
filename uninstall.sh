#!/bin/bash

# Server Status CLI Uninstaller
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
            L_START="🗑️  Starting Server Status CLI uninstallation..."
            L_BIN_DEL="✓ Executable removed"
            L_BIN_MISS="- Executable not found (already removed?)"
            L_VENV_DEL="✓ Virtual environment removed"
            L_VENV_MISS="- Virtual environment not found."
            L_DATA_WARN="⚠️  User data and configuration found in the project directory."
            L_DATA_ASK="❓ Do you want to delete your sites database (db.json) and config? (y/N): "
            L_DATA_DEL="✓ Data deleted. It was a pleasure serving you."
            L_DATA_KEEP="✓ Data preserved. If you reinstall, your sites will be there."
            L_DONE="✅ Uninstallation finished."
            break
            ;;
        "Español")
            L_START="🗑️  Iniciando desinstalación de Server Status CLI..."
            L_BIN_DEL="✓ Ejecutable eliminado"
            L_BIN_MISS="- Ejecutable no encontrado (ya eliminado?)"
            L_VENV_DEL="✓ Entorno virtual eliminado"
            L_VENV_MISS="- Entorno virtual no encontrado."
            L_DATA_WARN="⚠️  Se han encontrado datos de usuario y configuración en el directorio del proyecto."
            L_DATA_ASK="❓ ¿Quieres eliminar también la base de datos de sitios (db.json) y configuración? (s/N): "
            L_DATA_DEL="✓ Datos eliminados. Fue un placer servirte."
            L_DATA_KEEP="✓ Datos preservados. Si reinstalas, tus sitios seguirán ahí."
            L_DONE="✅ Desinstalación finalizada."
            break
            ;;
        *) echo "Invalid option / Opción inválida $REPLY";;
    esac
done

APP_DIR="$HOME/.server_status_cli_app"
BIN_FILE="$HOME/.local/bin/sstatus"
DB_BIN_FILE="$HOME/.local/bin/sstatus-db"
CONFIG_DIR="$HOME/.config/server-status-cli"

echo ""
echo "$L_START"

# 1. Borrar Binarios y Venv
for f in "$BIN_FILE" "$DB_BIN_FILE"; do
    if [ -f "$f" ]; then
        rm "$f"
        echo "$L_BIN_DEL ($f)"
    else
        echo "$L_BIN_MISS ($f)"
    fi
done

if [ -d "$APP_DIR" ]; then
    rm -rf "$APP_DIR"
    echo "$L_VENV_DEL ($APP_DIR)"
else
    echo "$L_VENV_MISS"
fi

# 2. Gestión de Datos (Interactivo)
if [ -d "$CONFIG_DIR" ]; then
    echo ""
    echo "$L_DATA_WARN"
    read -p "$L_DATA_ASK" -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        rm -rf "$CONFIG_DIR"
        echo "$L_DATA_DEL"
    else
        echo "$L_DATA_KEEP"
    fi
fi

echo ""
echo "$L_DONE"
