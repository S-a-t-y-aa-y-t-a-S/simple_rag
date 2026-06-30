
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.ingestion_router import IngestionRouter
from dependencies.yaml_extractor import YamlExtractor


app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# class init
ingestion_router = IngestionRouter(extractor=YamlExtractor())
app.include_router(router=ingestion_router.router)

