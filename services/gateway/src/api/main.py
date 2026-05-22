
from fastapi import FastAPI
from api.routers import ingestion_router

app = FastAPI()

app.include_router(router=ingestion_router.ingest)

