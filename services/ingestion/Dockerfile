# Base Image
FROM python:3.11-slim

# setting the env vars to keep python efficient
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /app

# Copying the contents of requirements.txt file and installing the dependencies with no cache
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copying rest of the content present in the service folder
COPY ./src ./src
COPY ./configs ./configs

#expose the port FastAPI runs on 
EXPOSE 8001

# Ingestion service is a celery worker, not HTTP server
# CMD starts the celery worker with worker entrypoint
CMD ["uvicorn", "src.api.main:app", "--port", "8001", "--reload"]

