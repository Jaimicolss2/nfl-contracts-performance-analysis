"""
Configuración central del proyecto
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
SQL_DIR = BASE_DIR / 'sql'
NOTEBOOKS_DIR = BASE_DIR / 'notebooks'
VIZ_DIR = BASE_DIR / 'visualizations'

# Configuración de base de datos
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'nfl_analysis')
}

# Temporadas a analizar
START_YEAR = 2019
END_YEAR = 2024
SEASONS = list(range(START_YEAR, END_YEAR + 1))

# Posiciones NFL
POSITIONS = {
    'offense': ['QB', 'RB', 'WR', 'TE', 'OL', 'OT', 'OG', 'C'],
    'defense': ['DL', 'DE', 'DT', 'LB', 'CB', 'S', 'DB'],
    'special': ['K', 'P', 'LS']
}

# Configuración de scraping
REQUEST_DELAY = 2  # segundos entre requests
USER_AGENT = 'Mozilla/5.0 (Educational Project)'

if __name__ == '__main__':
    print(f"[OK] Proyecto configurado correctamente")
    print(f"Base directory: {BASE_DIR}")
    print(f"Temporadas a analizar: {SEASONS}")