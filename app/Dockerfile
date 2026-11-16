# Builds the Python 3.12 container image, installs the PostgreSQL driver, and starts the web server
FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir "psycopg[binary]"
COPY main.py .
CMD ["python", "-u", "main.py"]