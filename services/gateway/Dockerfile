# base image
FROM python:3.11-slim

# setting env vars
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# working dir
WORKDIR /app

# copying the contents of requirements.txt
# and installing them
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copying the rest of the contents present in the service
COPY ./src ./src
COPY ./configs ./configs

#expose the port FastAPI runs on
EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--reload"]