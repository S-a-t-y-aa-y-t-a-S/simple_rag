
from fastapi import FastAPI
from api.routers.ingestion_router import IngestionRouter
from dependencies.yaml_extractor import YamlExtractor

app = FastAPI()

# class init
ingestion_router = IngestionRouter(extractor=YamlExtractor())
app.include_router(router=ingestion_router.router)

