from fastapi import FastAPI
from api.routes import route_ingestion

app = FastAPI()

app.include_router(router=route_ingestion.ingest)