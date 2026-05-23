from fastapi import FastAPI
from api.routes.route_ingestion import RouteIngestion
from dependencies.yaml_extractor import YamlExtractor

app = FastAPI()
extractor = YamlExtractor()

router_ingestion = RouteIngestion(extractor=extractor)
app.include_router(router=router_ingestion.router)