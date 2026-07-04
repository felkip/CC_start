import os
from dotenv import load_dotenv

load_dotenv()

# Exemplo de conexão com Supabase (comentado):
# Troque SENHA e o host db.xxx.supabase.co pelo valor real do seu projeto.
# DB_CONFIG = {
#     'dsn': 'postgresql://postgres:SENHA@db.xxx.supabase.co:5432/postgres?sslmode=require',
#     'sslmode': 'require'
# }

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
        return conn, None
    except psycopg2.Error as e:
        return None, str(e)

