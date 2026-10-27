import os
import mysql.connector
from mysql.connector import Error

def get_connect_kwargs(include_db=False):
    kwargs = {
        'host': os.environ.get('DB_HOST', 'localhost'),
        'user': os.environ.get('DB_USER', 'root'),
        'password': os.environ.get('DB_PASSWORD', '')
    }
    if include_db:
        kwargs['database'] = os.environ.get('DB_NAME', 'canteen_db')
    try:
        conn = mysql.connector.connect(**kwargs)
        if conn.is_connected():
            return conn
    except Error:
        pass
    return None

def create_database():
    try:
        conn = get_connect_kwargs(include_db=False)
        if conn and conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS canteen_db")
            print("Database 'canteen_db' created or already exists.")
            cursor.close()
            conn.close()
            return True
        else:
            print("Failed to connect to MySQL server.")
            return False
    except Error as e:
        print(f"Error connecting to MySQL Server: {e}")
        return False

def run_schema():
    try:
        conn = get_connect_kwargs(include_db=True)
        if conn and conn.is_connected():
            cursor = conn.cursor()
            schema_paths = [
                os.path.join(os.path.dirname(__file__), 'schema.sql'),
                'schema.sql',
                'canteen_app/schema.sql'
            ]
            schema_path = next((p for p in schema_paths if os.path.exists(p)), None)
            if not schema_path:
                print("Error: schema.sql not found.")
                return False
            with open(schema_path, 'r') as f:
                schema = f.read()

            # Split statements and execute
            statements = schema.split(';')
            for statement in statements:
                if statement.strip():
                    cursor.execute(statement)
            
            print("Schema executed successfully.")
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except Error as e:
        print(f"Error executing schema: {e}")
        return False

if __name__ == "__main__":
    if create_database():
        run_schema()
