import os
from dotenv import load_dotenv

load_dotenv()

# Configuração do PostgreSQL
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'cs_start'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', ''),
}

def get_db_connection():
    """Retorna uma conexão com o banco de dados."""
    import psycopg2
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None
