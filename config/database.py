import sqlite3
from sqlite3 import Connection, Cursor

class Database:
    ## Class to handle database operations using SQLite without external dependencies

    _instance = None
    _db_path = "clinica.db"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_connection(self) -> Connection:  # Returns a connection to the SQLite database
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row   #Premite acceder a las columnas por nombre.
        return conn

    def init_db(self) -> None:  # Initializes the database with necessary tables

        conn = self.get_connection()
        try: 
            cursor = conn.cursor()

            #Tabla Departamento
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamento (
                    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    piso INTEGER NOT NULL
                )
            """)

            #Tabla paciente
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS paciente (
                    rut TEXT NOT NULL,
                    nombre TEXT NOT NULL,
                    edad INTEGER NOT NULL,
                    prevision TEXT NOT NULL,
                    id_departamento INTEGER,
                    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento) ON DELETE SET NULL
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
        finally:
            conn.close()


if __name__ == "__main__":
    db = Database()
    db.init_db()
    print("Base de datos inicializada correctamente.")