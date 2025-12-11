# Modelo Entidad-Relación - Borrador Inicial

## Entidades Principales

### 1. JUGADORES
```
jugadores
---------
PK: jugador_id (INT)
    nombre (VARCHAR 100)
    fecha_nacimiento (DATE)
    universidad (VARCHAR 100)
    posicion (VARCHAR 10)
    draft_year (INT)
    draft_round (INT)
    draft_pick (INT)
    altura_cm (INT)
    peso_kg (DECIMAL)
    fecha_creacion (TIMESTAMP)
    fecha_actualizacion (TIMESTAMP)
```

### 2. EQUIPOS
```
equipos
-------
PK: equipo_id (INT)
    nombre (VARCHAR 100)
    ciudad (VARCHAR 50)
    conferencia (ENUM: AFC, NFC)
    division (ENUM: North, South, East, West)
    estadio (VARCHAR 100)
    fundacion (INT)
```

### 3. CONTRATOS
```
contratos
---------
PK: contrato_id (INT)
FK: jugador_id → jugadores
FK: equipo_id → equipos
    fecha_inicio (DATE)
    fecha_fin (DATE)
    valor_total (DECIMAL 12,2)
    guaranteed_money (DECIMAL 12,2)
    signing_bonus (DECIMAL 12,2)
    avg_annual_value (DECIMAL 12,2)
    tipo_contrato (ENUM: Rookie, Extension, Free Agent)
    estado (ENUM: Active, Completed, Terminated)
```

### 4. ESTADISTICAS_TEMPORADA
```
estadisticas_temporada
----------------------
PK: stat_id (INT)
FK: jugador_id → jugadores
FK: equipo_id → equipos
    temporada (INT)
    juegos_jugados (INT)
    juegos_iniciados (INT)
    
    # QB Stats
    pases_completados (INT)
    pases_intentados (INT)
    yardas_pase (INT)
    touchdowns_pase (INT)
    intercepciones (INT)
    qb_rating (DECIMAL 5,2)
    
    # RB Stats
    carreras (INT)
    yardas_terrestres (INT)
    td_terrestres (INT)
    
    # WR/TE Stats
    recepciones (INT)
    targets (INT)
    yardas_recepcion (INT)
    td_recepciones (INT)
    
    # DEF Stats
    tackles_totales (INT)
    sacks (DECIMAL 4,1)
    intercepciones_def (INT)
    fumbles_forzados (INT)
```

### 5. SALARY_CAP
```
salary_cap
----------
PK: cap_id (INT)
    temporada (INT) UNIQUE
    cap_total (DECIMAL 12,2)
    cap_minimo (DECIMAL 12,2)
    cap_penalty_avg (DECIMAL 12,2)
```

### 6. RECORD_EQUIPOS
```
record_equipos
--------------
PK: record_id (INT)
FK: equipo_id → equipos
    temporada (INT)
    victorias (INT)
    derrotas (INT)
    empates (INT)
    playoffs (BOOLEAN)
    super_bowl (BOOLEAN)
    puntos_favor (INT)
    puntos_contra (INT)
```

## Relaciones

- Un JUGADOR puede tener múltiples CONTRATOS (1:N)
- Un EQUIPO puede tener múltiples CONTRATOS (1:N)
- Un JUGADOR tiene múltiples ESTADISTICAS_TEMPORADA (1:N)
- Un EQUIPO tiene múltiples RECORD_EQUIPOS (1:N)
- Cada TEMPORADA tiene un único SALARY_CAP (1:1)

## Próximos pasos

1. Validar modelo con datos reales
2. Crear diagrama visual (Draw.io o dbdiagram.io)
3. Implementar en SQL