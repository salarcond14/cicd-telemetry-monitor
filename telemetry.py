import os
import requests
import json
from datetime import datetime

# --- CONFIGURACIÓN ---
GITHUB_USER = "salarcond14"          # Ej. "SantiagoAlarcon"
REPO_NAME = "cicd-telemetry-monitor"          # El repositorio que creamos
TOKEN = os.getenv("GITHUB_TOKEN") or input("Ingresa tu GitHub Token: ").strip()
# Configuración de cabeceras HTTP exigidas por la API de GitHub
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Endpoint oficial de la REST API de GitHub para los workflows runs
url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/actions/runs"

print(f"🔍 Conectando con la API de GitHub para el repositorio: {REPO_NAME}...\n")
response = requests.get(url, headers=headers)

# Verificamos si la conexión fue exitosa (Código HTTP 200)
if response.status_code == 200:
    data = response.json()
    total_runs_count = data.get("total_count", 0)
    runs = data.get("workflow_runs", [])
    
    print(f"¡Conexión exitosa! Se encontraron {total_runs_count} ejecuciones en total.\n")
    print("=" * 60)
    
    success_count = 0
    failure_count = 0
    
    # Analizamos cada ejecución obtenida
    for index, run in enumerate(runs, start=1):
        run_id = run.get('id')
        event = run.get('event')
        status = run.get('status')         # completed, in_progress, queued
        conclusion = run.get('conclusion') # success, failure, cancelled
        created_at = run.get('created_at')
        head_commit = run.get('head_commit', {}).get('message', 'No message')
        
        # Conteo de éxitos y fallos
        if conclusion == 'success':
            success_count += 1
        elif conclusion == 'failure':
            failure_count += 1
            
        print(f"[{index}] Run ID: {run_id}")
        print(f"    - Evento: {event} | Estado: {status} ({conclusion})")
        print(f"    - Commit: {head_commit.strip()}")
        print(f"    - Fecha: {created_at}")
        print("-" * 60)

    # Cálculo de Métricas (Observabilidad básica)
    if len(runs) > 0:
        success_rate = (success_count / len(runs)) * 100
        print("\n --- MÉTRICAS DE INFRAESTRUCTURA (TELEMETRY) ---")
        print(f"• Total analizado: {len(runs)} builds")
        print(f"• Builds exitosos: {success_count}")
        print(f"• Builds fallidos: {failure_count}")
        print(f"• Tasa de éxito (Success Rate): {success_rate:.2f}%")
        print("--------------------------------------------------")
        
        # Opcional: Guardar este reporte directamente en un archivo Markdown para el repositorio
        report_content = f"""# 📊 CI/CD Telemetry Report
*Generado automáticamente el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

- **Total Builds Analizados:** {len(runs)}
- **Builds Exitosos:** {success_count}
- **Builds Fallidos:** {failure_count}
- **Success Rate:** {success_rate:.2f}%
"""
        with open("ci_report.md", "w", encoding="utf-8") as report_file:
            report_file.write(report_content)
        print("\n¡Reporte generado exitosamente en 'ci_report.md'!")
        
else:
    print(f"Error al conectar con la API de GitHub. Código HTTP: {response.status_code}")
    print(response.text)