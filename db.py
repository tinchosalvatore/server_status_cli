import json
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

# Constantes
DB_FILE = "db.json"
console = Console()

def load_db() -> list[dict[str, str]]:
    """Carga la base de datos desde el archivo JSON."""
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        console.print("[bold red]⚠ Error al leer el archivo JSON. Se iniciará una lista vacía.[/]")
        return []

def save_db(data: list[dict[str, str]]):
    """Guarda la lista actualizada en el archivo JSON."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    console.print(f"[green]✔ Base de datos guardada en {DB_FILE}[/green]")

def list_sites(data: list[dict[str, str]]):
    """Muestra la tabla actual de sitios configurados."""
    if not data:
        console.print(Panel("La base de datos está vacía.", style="yellow"))
        return

    table = Table(title="Sitios Configurados")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Cliente", style="magenta")
    table.add_column("Servicio", style="white")
    table.add_column("URL", style="green")

    for idx, site in enumerate(data):
        table.add_row(str(idx + 1), site["client"], site["name"], site["url"])

    console.print(table)

def add_site(current_data: list[dict[str, str]]):
    """Interactivamente agrega un nuevo sitio."""
    console.print("\n[bold cyan]Agregar Nuevo Sitio[/bold cyan]")
    
    client = Prompt.ask("👤 Nombre del Cliente")
    name = Prompt.ask("🏷️  Nombre del Servicio (ej. Landing, API)")
    
    # Validación simple de URL
    while True:
        url = Prompt.ask("🔗 URL del sitio")
        if url.startswith("http://") or url.startswith("https://"):
            break
        console.print("[red]La URL debe comenzar con http:// o https://[/red]")

    new_entry = {"client": client, "name": name, "url": url}
    current_data.append(new_entry)
    save_db(current_data)
    console.print("[bold green]Sitio agregado exitosamente![/]")

def delete_site(current_data: list[dict[str, str]]):
    """Elimina un sitio seleccionado por su ID."""
    if not current_data:
        console.print("[yellow]⚠ No hay sitios para eliminar.[/]")
        return

    # Mostramos la lista primero para que vea el ID
    list_sites(current_data)
    
    console.print("\n[bold red]Eliminar Sitio[/bold red]")
    choice = Prompt.ask("Ingresa el [cyan]ID[/] del sitio a borrar (o 'c' para cancelar)")

    if choice.lower() == 'c':
        return

    try:
        idx = int(choice) - 1
        if 0 <= idx < len(current_data):
            removed = current_data.pop(idx)
            save_db(current_data)
            console.print(f"[bold red]🗑️ Sitio eliminado: {removed['name']} ({removed['url']})[/]")
        else:
            console.print("[red]❌ ID inválido.[/]")
    except ValueError:
        console.print("[red]❌ Debes ingresar un número.[/]")

def main():
    console.print(Panel("[bold blue]🔧 Monitor Manager v1.1[/bold blue]", expand=False))
    
    while True:
        data = load_db()
        console.print("\n[1] Agregar sitio  [2] Listar sitios  [3] Eliminar sitio  [4] Salir")
        choice = Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4"], default="1")

        if choice == "1":
            add_site(data)
        elif choice == "2":
            list_sites(data)
        elif choice == "3":
            delete_site(data)
        elif choice == "4":
            console.print("[italic]Hasta luego![/italic]")
            break

if __name__ == "__main__":
    main()