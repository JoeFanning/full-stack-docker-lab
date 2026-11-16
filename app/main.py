# Lightweight Python HTTP server that logs each page visit into PostgreSQL and renders the visit history
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg

CONN_INFO = (
    f"host=db "
    f"dbname={os.environ['POSTGRES_DB']} "
    f"user={os.environ['POSTGRES_USER']} "
    f"password={os.environ['POSTGRES_PASSWORD']}"
)

# Wait for Postgres to finish starting up and create the visits table
for _ in range(15):
    try:
        with psycopg.connect(CONN_INFO) as conn:
            with conn.cursor() as cur:
                cur.execute("CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, ts timestamptz DEFAULT now());")
        break
    except psycopg.OperationalError:
        time.sleep(1)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        with psycopg.connect(CONN_INFO) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO visits DEFAULT VALUES;")
                cur.execute("SELECT id, ts FROM visits ORDER BY id DESC LIMIT 10;")
                rows = cur.fetchall()

        body = "<h1>Docker Full-Stack Lab</h1><ul>"
        for row_id, ts in rows:
            body += f"<li>Visit #{row_id} at {ts}</li>"
        body += "</ul>"

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()