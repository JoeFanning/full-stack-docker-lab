NEXT STEPS 16/11/26

1. Document the Repo (README.md)
Adding a short README.md at the root of your project gives you an instant quick-reference guide on GitHub when you clone this project onto another machine later. Create README.md in your root folder, add setup instructions (cp .env.example .env followed by docker compose up --build -d), and push it from PyCharm (Ctrl + K to commit, Ctrl + Shift + K to push).

2. Upgrade the Python Backend to FastAPI
Your current app/main.py uses Python's built-in http.server to prove the container wiring works. To turn this template into a production-ready backend:

Swap http.server for FastAPI and Uvicorn (pip install fastapi uvicorn[standard] "psycopg[binary]").

Add a requirements.txt inside app/ so app/Dockerfile installs dependencies cleanly via RUN pip install --no-cache-dir -r requirements.txt.

Add a GET /health endpoint so Docker Compose and NGINX can monitor container readiness automatically.

3. Practice Everyday Docker & Database Operations
Before shutting things down for the night, test how your stack handles persistence and live updates:

Inspect PostgreSQL directly:

PowerShell
docker compose exec db psql -U admin -d appdb -c "SELECT * FROM visits;"
Shut down without losing data:

PowerShell
docker compose down
(Your pgdata volume stays intact on disk; running docker compose up -d later brings your exact visit history back. Only docker compose down -v wipes the database volume.)

 
