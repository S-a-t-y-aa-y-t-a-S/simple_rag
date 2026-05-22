
from fastapi import status, APIRouter, UploadFile, Depends
from core.ingestion_service.ingestion import forward_file
from dependencies.service_clients import get_ingestion_client
from api.schemas.ingestion_schema import IngestResponse
from dependencies.yaml_extractor import YamlExtractor

url_config = YamlExtractor().get_url_config()

ingest = APIRouter(
    prefix=url_config.endpoint,
    tags=[url_config.tag]
)

@ingest.post(path=url_config.base_endpoint, status_code=status.HTTP_201_CREATED)
async def call_ingestion_service(uploaded_file: UploadFile, 
                                 client=Depends(get_ingestion_client)):
    response = await forward_file(
        uploaded_file=uploaded_file,
        client=client
    )    

    return IngestResponse(
        status=response.status_code,
        message=response.text,
        content=response.json()
    )