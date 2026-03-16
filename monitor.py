import asyncio
import time
import json
import os
import sys
import argparse
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

import httpx
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.live import Live

from report import generate_report
from i18n import _

# Configuración
DB_FILE = "db.json"
REFRESH_RATE = 10  # Segundos entre chequeos
console = Console()

@dataclass
class CheckResult:
    client: str
    name: str
    url: str
    status_code: int | str
    latency: float
    is_success: bool
    error_msg: str = ""

class UptimeMonitor:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.sites: List[Dict[str, str]] = []

    def load_sites(self) -> bool:
        """Carga sitios. Retorna False si no hay archivo."""
        if not os.path.exists(self.db_path):
            return False
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                self.sites = json.load(f)
            return True
        except json.JSONDecodeError:
            return False

    async def check_site(self, client: httpx.AsyncClient, site: Dict[str, str]) -> CheckResult:
        start_time = time.perf_counter()
        url = site["url"]
        
        try:
            response = await client.get(url, timeout=5.0, follow_redirects=True)
            latency = (time.perf_counter() - start_time) * 1000
            is_success = response.status_code == 200
            
            result = CheckResult(
                client=site.get("client", "Unknown"),
                name=site.get("name", "Service"),
                url=url,
                status_code=response.status_code,
                latency=latency,
                is_success=is_success
            )

        except httpx.RequestError as e:
            latency = (time.perf_counter() - start_time) * 1000
            result = CheckResult(
                client=site.get("client", "Unknown"),
                name=site.get("name", "Service"),
                url=url,
                status_code="ERR",
                latency=latency,
                is_success=False,
                error_msg=str(e)
            )
        
        return result

    def generate_table(self, results: List[CheckResult]) -> Table:
        """Genera la tabla Rich basada en resultados."""
        table = Table(show_header=True, header_style="bold white", border_style="dim", expand=True)
        table.add_column(_("col_client"), style="cyan")
        table.add_column(_("col_service"), style="white")
        table.add_column(_("col_status"), justify="center")
        table.add_column(_("col_code"), justify="right")
        table.add_column(_("col_latency"), justify="right")

        errors_found = False

        for res in results:
            if res.is_success:
                status_icon = "✅"
                row_style = "green"
            else:
                status_icon = "❌"
                row_style = "bold red"
                errors_found = True

            latency_str = f"{res.latency:.0f} ms"
            if res.latency > 1000:
                latency_str = f"[bold red]{latency_str}[/]"
            elif res.latency > 500:
                latency_str = f"[yellow]{latency_str}[/]"

            table.add_row(
                res.client,
                res.name,
                status_icon,
                str(res.status_code),
                latency_str,
                style=row_style
            )

        # Alerta sonora si hay errores (System Beep)
        if errors_found:
            print("\a") 

        return table

    async def run_loop(self):
        if not self.load_sites():
            console.print(f"[red]{_('error_db_not_found')}[/]")
            return

        console.clear()
        console.print(f"[bold yellow]{_('starting_monitor')}[/]")

        # Usamos Live de Rich para actualizar la tabla en el mismo lugar
        with Live(console=console, refresh_per_second=4) as live:
            while True:
                # Recargamos sitios en cada vuelta por si editaste el JSON mientras corría
                self.load_sites()
                
                async with httpx.AsyncClient() as client:
                    tasks = [self.check_site(client, site) for site in self.sites]
                    results = await asyncio.gather(*tasks)

                # Construimos el layout
                now = datetime.now().strftime("%H:%M:%S")
                table = self.generate_table(results)
                
                panel = Panel(
                    Align.center(table),
                    title=f"[bold cyan]🚀 {_('monitor_title')} - {now}[/]",
                    subtitle=f"[dim]{_('next_update')} {REFRESH_RATE}s | tool by tinchosalvatore[/]",
                    border_style="blue"
                )
                
                live.update(panel)
                
                # Espera asíncrona
                await asyncio.sleep(REFRESH_RATE)

    async def run_once(self) -> List[CheckResult] | None:
        """Ejecuta un único chequeo y retorna los resultados."""
        if not self.load_sites():
            console.print(f"[red]{_('error_db_not_found')}[/]")
            return None

        console.print(f"[yellow]{_('checking_once')}[/]")

        async with httpx.AsyncClient() as client:
            tasks = [self.check_site(client, site) for site in self.sites]
            results = await asyncio.gather(*tasks)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        table = self.generate_table(results)
        
        panel = Panel(
            Align.center(table),
            title=f"[bold cyan]🚀 {_('monitor_status')} - {now}[/]",
            border_style="blue"
        )
        
        console.print(panel)
        return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor de estado de sitios web.")
    parser.add_argument("-f", "--fast", action="store_true", help="Si se especifica, ejecuta el chequeo una sola vez y sale.")
    parser.add_argument("-r", "--report", action="store_true", help="Genera un reporte HTML con el estado actual.")
    args = parser.parse_args()

    monitor = UptimeMonitor(DB_FILE)

    try:
        if args.report:
            results = asyncio.run(monitor.run_once())
            if results:
                # Convertimos los objetos CheckResult a dicts
                results_dicts = [asdict(r) for r in results]
                report_path = generate_report(results_dicts)
                console.print(f"\n[bold green]{_('report_success')}[/bold green] [cyan]{os.path.abspath(report_path)}[/]")
        elif args.fast:
            asyncio.run(monitor.run_once())
        else:
            asyncio.run(monitor.run_loop())
    except KeyboardInterrupt:
        console.clear()
        console.print(f"\n[bold green]{_('stop_monitor')}[/]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[bold red]{_('unexpected_error')} {e}[/]")
        sys.exit(1)
