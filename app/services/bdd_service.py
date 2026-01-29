import psycopg2
from psycopg2.extras import RealDictCursor
import time

class BddService:
    def __init__(self, host="db", database="botdb", user="user", password="password", port=5432):
        self.conn_params = {
            "host": host,
            "database": database,
            "user": user,
            "password": password,
            "port": port
        }
        self.conn = self._connect_with_retry()
        self._setup_tables()

    def _connect_with_retry(self):
        while True:
            try:
                conn = psycopg2.connect(**self.conn_params)
                print("Connexion à PostgreSQL réussie !")
                return conn
            except psycopg2.OperationalError:
                print("La BDD n'est pas prête, nouvelle tentative dans 2 secondes...")
                time.sleep(2)

    def _setup_tables(self):
        """Crée la structure initiale."""
        with self.conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS citations (
                    id SERIAL PRIMARY KEY, 
                    texte TEXT NOT NULL
                )
            """)
            # Vérification si vide
            cursor.execute("SELECT count(*) FROM citations")
            if cursor.fetchone()[0] == 0:
                citations = [
                    ("La persévérance est la clé du succès.",),
                    ("Le code est comme l'humour, s'il faut l'expliquer, c'est qu'il est mauvais.",),
                    ("Hello World!",)
                ]
                cursor.executemany("INSERT INTO citations (texte) VALUES (%s)", citations)
            self.conn.commit()

    def get_random_citation(self):
        """Récupère une citation au hasard."""
        with self.conn.cursor() as cursor:
            # PostgreSQL utilise 'RANDOM()' au lieu de 'RANDOM()' (SQLite)
            cursor.execute("SELECT texte FROM citations ORDER BY RANDOM() LIMIT 1")
            result = cursor.fetchone()
            return result[0] if result else "Pas de données."

    def close(self):
        if self.conn:
            self.conn.close()