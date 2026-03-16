import os
import json
from datetime import datetime
from typing import List
from jinja2 import Environment, FileSystemLoader
from i18n import get_all_strings

def get_latency_class(latency: float) -> str:
    """Retorna una clase CSS basada en la latencia."""
    if latency > 1000:
        return "latency-slow"
    if latency > 500:
        return "latency-medium"
    return "latency-fast"

def generate_report(results: List[dict], output_dir: str = "reports"):
    """
    Genera un reporte HTML a partir de una lista de resultados de chequeo.
    """
    # 1. Asegurar que el directorio de reportes exista
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. Configurar Jinja2
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    # 3. Obtener traducciones
    i18n = get_all_strings()

    # 4. Procesar datos para la plantilla
    total_services = len(results)
    total_up = sum(1 for r in results if r['is_success'])
    total_down = total_services - total_up

    # Añadir información de estilo de latencia y status localizado
    for result in results:
        result['latency_class'] = get_latency_class(result['latency'])
        result['status_label'] = i18n['report_status_online'] if result['is_success'] else i18n['report_status_offline']

    # 5. Renderizar la plantilla
    html_content = template.render(
        results=results,
        total_services=total_services,
        total_up=total_up,
        total_down=total_down,
        generation_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        i18n=i18n
    )

    # 6. Guardar el archivo
    report_filename = f"uptime_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    report_path = os.path.join(output_dir, report_filename)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Copiar el CSS al directorio del reporte para que sea autocontenido
    css_source_path = "templates/style.css"
    css_dest_path = os.path.join(output_dir, "style.css")
    if os.path.exists(css_source_path):
        with open(css_source_path, "r", encoding="utf-8") as f_in, \
             open(css_dest_path, "w", encoding="utf-8") as f_out:
            f_out.write(f_in.read())
            
    return report_path
