# FROM python:3.12-slim --> Pulls the official Python 3.12 image from Docker Hub. 
# The slim variant uses a stripped-down Debian Linux distribution, 
# keeping the container image size small while still providing a reliable Python runtime environment.
FROM python:3.12-slim
# WORKDIR /app --> Working Directory: Sets /app as the active directory inside the container. Any subsequent 
# commands (RUN, COPY, CMD) will run relative to this path, and files will be copied here.
WORKDIR /app
# RUN pip install --no-cache-dir "psycopg[binary]" -->
# psycopg[binary]: This is the software package (the bridge) your Python code uses to send queries and talk to PostgreSQL. 
# The [binary] part means it comes pre-packaged, so it installs 
# quickly without needing extra compilation tools.
# --no-cache-dir: When pip downloads a package, it normally saves temporary backup files (a cache) on your hard drive 
# just in case you need them again. Inside a Docker container, you don't need those backups cluttering up space. 
# This flag tells pip to throw away those temporary files immediately, keeping your final Docker image smaller and lighter.
RUN pip install --no-cache-dir "psycopg[binary]"
# COPY main.py -->
# File Copy: Copies your local main.py file from your host machine's(your computer or a server on line) app/ directory into 
# the container's current working directory (/app/.).
COPY main.py .
# CMD ["python", "-u", "main.py"]
# Default Execution Command: Tells the container what command to run when it starts up. It executes Python to run your script.
# Note on flags: The -u flag runs Python in unbuffered mode. This ensures that print statements and error logs are sent straight 
# to the Docker console immediately without sitting in a buffer, making it much easier to monitor your app logs in real time.
CMD ["python", "-u", "main.py"]
