from django.http import HttpResponse
import psycopg2

def init(request):
    try:
        # Connexion à la base de données PostgreSQL
        conn = psycopg2.connect(
            dbname="formationdjango",
            user="djangouser",
            password="secret",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Création de la table si elle n'existe pas déjà
        create_table_query = """
        CREATE TABLE IF NOT EXISTS ex00_movies (
            episode_nb SERIAL PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """
        cur.execute(create_table_query)

        # Valider et fermer la connexion
        conn.commit()
        cur.close()
        conn.close()

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
