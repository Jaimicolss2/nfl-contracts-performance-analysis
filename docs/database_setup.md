# Configuración de Base de Datos

## Opción 1: MySQL

### Instalación en Windows

1. Descargar MySQL Community Server: https://dev.mysql.com/downloads/mysql/
2. Ejecutar el instalador
3. Durante instalación:
   - Tipo: Developer Default
   - Configurar contraseña de root
4. Verificar que MySQL esté corriendo:
```bash
   mysql --version
```

### Crear base de datos

Abrir terminal y ejecutar:
```bash
mysql -u root -p
```

Ejecutar estos comandos SQL:
```sql
CREATE DATABASE nfl_analysis CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'nfl_user'@'localhost' IDENTIFIED BY 'tu_password_seguro';
GRANT ALL PRIVILEGES ON nfl_analysis.* TO 'nfl_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### Configurar variables de entorno

Editar el archivo `.env` en la raíz del proyecto:
```
DB_HOST=localhost
DB_PORT=3306
DB_USER=nfl_user
DB_PASSWORD=tu_password_seguro
DB_NAME=nfl_analysis
```

---

## Opción 2: PostgreSQL

### Instalación en Windows

1. Descargar desde: https://www.postgresql.org/download/
2. Ejecutar instalador
3. Recordar la contraseña que configures para el usuario postgres

### Crear base de datos
```bash
psql -U postgres
```
```sql
CREATE DATABASE nfl_analysis;
CREATE USER nfl_user WITH PASSWORD 'tu_password_seguro';
GRANT ALL PRIVILEGES ON DATABASE nfl_analysis TO nfl_user;
\q
```

### Configurar variables de entorno
```
DB_HOST=localhost
DB_PORT=5432
DB_USER=nfl_user
DB_PASSWORD=tu_password_seguro
DB_NAME=nfl_analysis
```

---

## Verificar conexión (cuando instales la BD)

Crear archivo `test_connection.py` en la raíz:
```python
from sqlalchemy import create_engine, text
from src.config import DB_CONFIG

# Para MySQL
connection_string = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

# Para PostgreSQL (descomentar si usas PostgreSQL)
# connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

try:
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("[OK] Conexion exitosa a la base de datos")
except Exception as e:
    print(f"[ERROR] No se pudo conectar: {e}")
```

Ejecutar:
```bash
python test_connection.py
```

---

## Notas

- La instalación de MySQL/PostgreSQL se hará en la Fase 2
- Por ahora, solo documentamos el proceso
- Cuando instales, vuelve a este documento