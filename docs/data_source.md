# Fuentes de Datos del Proyecto

## 1. Spotrac (https://www.spotrac.com/nfl/)

### Datos disponibles:
- Contratos detallados de jugadores actuales
- Información histórica de contratos
- Detalles de dinero garantizado, bonos de firma
- Dead money y reestructuraciones

### Método de obtención:
- Web scraping con BeautifulSoup
- Datos públicos sin API oficial
- Respetar rate limits y robots.txt

### Tablas objetivo:
- `contratos`
- `equipos`
- `salary_cap`

---

## 2. Pro Football Reference (https://www.pro-football-reference.com/)

### Datos disponibles:
- Estadísticas completas por jugador y temporada
- Datos desde 1920 hasta presente
- Advanced stats (AV - Approximate Value)
- Información de draft

### Método de obtención:
- Web scraping
- Estructura HTML consistente
- Datos bien documentados

### Tablas objetivo:
- `jugadores`
- `estadisticas_temporada`

---

## 3. Over The Cap (https://overthecap.com/)

### Datos disponibles:
- Salary cap space por equipo
- Proyecciones de cap futuro
- Dead money y cap hits

### Método de obtención:
- Web scraping
- Complementa datos de Spotrac

### Tablas objetivo:
- `salary_cap`
- `contratos`

---

## 4. ESPN API (No oficial)

### Datos disponibles:
- Datos en tiempo real
- Schedules y resultados
- Roster updates

### Método de obtención:
- Endpoints públicos no documentados oficialmente
- Usar con precaución

### Documentación útil:
- https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b

---

## 5. Kaggle Datasets

### Datasets relevantes:
- "NFL Player Stats" (históricos)
- "NFL Salaries 1985-2020"
- Buscar: https://www.kaggle.com/search?q=nfl

### Método de obtención:
- Descarga directa
- Kaggle API

---

## 6. nfl-data-py (Librería Python)

### Instalación:
```bash
pip install nfl-data-py
```

### Datos disponibles:
- Play-by-play data
- Rosters
- Player stats
- Draft picks

### Documentación:
- https://github.com/nfl-data-py/nfl_data_py

---

## Consideraciones Éticas y Legales

1. **Respetar Terms of Service** de cada sitio
2. **Rate Limiting**: No sobrecargar servidores
3. **Robots.txt**: Verificar permisos de scraping
4. **Atribución**: Citar fuentes en análisis
5. **Uso educativo**: Este proyecto es con fines de portafolio

## Plan de Extracción - Prioridades

### Fase inicial (datos mínimos viables):
1. Descargar dataset de Kaggle para datos históricos base
2. Usar nfl-data-py para datos recientes (2022-2024)

### Fase avanzada:
3. Implementar scraping de Spotrac para contratos actualizados
4. Scraping de Pro Football Reference para stats faltantes