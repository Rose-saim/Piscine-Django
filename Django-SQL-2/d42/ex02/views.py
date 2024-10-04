# ex02/views.py
import psycopg2
from django.http import HttpResponse

def init(request):
    try:
        conn = psycopg2.connect(
            dbname="formationdjango",
            user="djangouser",
            password="secret",
            host="localhost"
        )
        curr = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS ex02_movies (
            episode_nb SERIAL PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """
        curr.execute(query)
        conn.commit()
        curr.close()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))
# ex02/views.py
def populate(request):
    data = [
        (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
        (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
    ]

    try:
        conn = psycopg2.connect(
            dbname="formationdjango",
            user="djangouser",
            password="secret",
            host="localhost"
        )
        curr = conn.cursor()
        response = ""
        for episode_nb, title, director, producer, release_date in data:
            try:
                curr.execute("""
                    INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s);
                """, (episode_nb, title, director, producer, release_date))
                response += f"Inserted {title}: OK<br>"
            except Exception as e:
                response += f"Error inserting {title}: {str(e)}<br>"
        conn.commit()
        curr.close()
        conn.close()
        return HttpResponse(response)
    except Exception as e:
        return HttpResponse(str(e))
# ex02/views.py
def display(request):
    try:
        conn = psycopg2.connect(
            dbname="formationdjango",
            user="djangouser",
            password="secret",
            host="localhost"
        )
        curr = conn.cursor()
        curr.execute("SELECT * FROM ex02_movies;")
        rows = curr.fetchall()
        if not rows:
            return HttpResponse("No data available")
        table = "<table><tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
        for row in rows:
            table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td></tr>"
        table += "</table>"
        curr.close()
        conn.close()
        return HttpResponse(table)
    except Exception as e:
        return HttpResponse(str(e))
