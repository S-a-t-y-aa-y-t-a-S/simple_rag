# Base Image
FROM python:3.11-slim

# Working directory inside the container
WORKDIR /app

# Copying the contents of requirements.txt file and installing the dependencies with no cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copying rest of the content present in the service folder
COPY . .

# Ingestion service is a celery worker, not HTTP server
# CMD starts the celery worker with worker entrypoint
CMD ["uvicorn", "api.main:app", "--port", "8001", "--reload"]

