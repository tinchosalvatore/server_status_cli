import json
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

from i18n import _

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
        console.print(f"[bold red]{_('db_read_error')}[/]")
        return []

def save_db(data: list[dict[str, str]]):
    """Guarda la lista actualizada en el archivo JSON."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    console.print(f"[green]{_('db_save_success')} {DB_FILE}[/green]")

def list_sites(data: list[dict[str, str]]):
    """Muestra la tabla actual de sitios configurados."""
    if not data:
        console.print(Panel(_('db_empty'), style="yellow"))
        return

    table = Table(title=_('db_table_title'))
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column(_("col_client"), style="magenta")
    table.add_column(_("col_service"), style="white")
    table.add_column("URL", style="green")

    for idx, site in enumerate(data):
        table.add_row(str(idx + 1), site["client"], site["name"], site["url"])

    console.print(table)

def add_site(current_data: list[dict[str, str]]):
    """Interactivamente agrega un nuevo sitio."""
    console.print(f"\n[bold cyan]{_('db_add_title')}[/bold cyan]")
    
    client = Prompt.ask(_('db_prompt_client'))
    name = Prompt.ask(_('db_prompt_service'))
    
    # Validación simple de URL
    while True:
        url = Prompt.ask(_('db_prompt_url'))
        if url.startswith("http://") or url.startswith("https://"):
            break
        console.print(f"[red]{_('db_url_error')}[/red]")

    new_entry = {"client": client, "name": name, "url": url}
    current_data.append(new_entry)
    save_db(current_data)
    console.print(f"[bold green]{_('db_add_success')}[/]")

def delete_site(current_data: list[dict[str, str]]):
    """Elimina un sitio seleccionado por su ID."""
    if not current_data:
        console.print(f"[yellow]{_('db_no_sites_delete')}[/]")
        return

    # Mostramos la lista primero para que vea el ID
    list_sites(current_data)
    
    console.print(f"\n[bold red]{_('db_delete_title')}[/bold red]")
    choice = Prompt.ask(_('db_delete_prompt'))

    if choice.lower() == 'c':
        return

    try:
        idx = int(choice) - 1
        if 0 <= idx < len(current_data):
            removed = current_data.pop(idx)
            save_db(current_data)
            console.print(f"[bold red]{_('db_delete_success')} {removed['name']} ({removed['url']})[/]")
        else:
            console.print(f"[red]{_('db_invalid_id')}[/red]")
    except ValueError:
        console.print(f"[red]{_('db_invalid_number')}[/red]")

def main():
    console.print(Panel(
        f"[bold blue]{_('db_manager_title')}[/bold blue]", 
        subtitle="[dim]tool by tinchosalvatore[/]",
        expand=False
    ))
    
    while True:
        data = load_db()
        menu_text = f"\n[1] {_('db_menu_1')}  [2] {_('db_menu_2')}  [3] {_('db_menu_3')}  [4] {_('db_menu_4')}"
        console.print(menu_text)
        choice = Prompt.ask(_('db_menu_option'), choices=["1", "2", "3", "4"], default="1")

        if choice == "1":
            add_site(data)
        elif choice == "2":
            list_sites(data)
        elif choice == "3":
            delete_site(data)
        elif choice == "4":
            console.print(f"[italic]{_('db_bye')}[/italic]")
            break

if __name__ == "__main__":
    main()