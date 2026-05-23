
from fastapi import FastAPI
from api.routers.ingestion_router import IngestionRouter
from dependencies.yaml_extractor import YamlExtractor

app = FastAPI()
extractor = YamlExtractor()

# class init
ingestion_router = IngestionRouter(extractor=extractor)
app.include_router(router=ingestion_router.router)

