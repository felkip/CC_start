import bcrypt
import psycopg2
from config.db_config import get_db_connection

def hash_password(password):
    """Cria hash da senha."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, password_hash):
    """Verifica se a senha corresponde ao hash."""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

def register_user(username, email, password):
    """Registra um novo usuário."""
    conn, error = get_db_connection()
    if not conn:
        return False, f"Erro ao conectar ao banco de dados: {error}"
    
    try:
        cursor = conn.cursor()
        password_hash = hash_password(password)
        
        cursor.execute(
            """
            INSERT INTO usuarios (nome_usuario, email, senha_hash)
            VALUES (%s, %s, %s)
            """,
            (username, email, password_hash)
        )
        
        conn.commit()
        cursor.close()
        conn.close()
        return True, "Usuário registrado com sucesso!"
        
    except psycopg2.IntegrityError:
        conn.close()
        return False, "Nome de usuário ou email já existem"
    except Exception as e:
        conn.close()
        return False, f"Erro ao registrar: {str(e)}"

def login_user(username, password):
    """Faz login de um usuário."""
    conn, error = get_db_connection()
    if not conn:
        return False, None, f"Erro ao conectar ao banco de dados: {error}"
    
    try:
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT id_usuario, senha_hash FROM usuarios WHERE nome_usuario = %s",
            (username,)
        )
        
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if not result:
            return False, None, "Usuário não encontrado"
        
        user_id, password_hash = result
        
        if verify_password(password, password_hash):
            return True, user_id, "Login bem-sucedido!"
        else:
            return False, None, "Senha incorreta"
            
    except Exception as e:
        conn.close()
        return False, None, f"Erro ao fazer login: {str(e)}"
