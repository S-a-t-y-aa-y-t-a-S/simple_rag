
from fastapi import status, APIRouter, UploadFile, Depends, File
from core.ingestion_service.ingestion import IngestionService
from dependencies.service_clients import ServiceClients
from api.schemas.ingestion_schema import IngestResponse
from dependencies.yaml_extractor import YamlExtractor
import httpx


class IngestionRouter:

    def __init__(self, extractor: YamlExtractor):
        self._url_config = extractor.get_url_config()
        self._ingestion_serv_config = extractor.get_ingestion_service_config()
        self.router = APIRouter(
            prefix=self._ingestion_serv_config.endpoint,
            tags=[self._ingestion_serv_config.tag]
        )
        
        self._register_routes()

    def _register_routes(self):

        self.router.add_api_route(
            path=self._url_config.base_endpoint,
            endpoint=self._call_ingestion_service,
            methods=[self._ingestion_serv_config.api_method],
            status_code=status.HTTP_201_CREATED,
            response_model=IngestResponse
        )

    async def _call_ingestion_service(
            self,
            uploaded_file: UploadFile = File(...),
            client:httpx.AsyncClient=Depends(ServiceClients().get_ingestion_client) 
    ):

        response = await IngestionService().forward_file(
            uploaded_file=uploaded_file,
            client=client
        )

        return IngestResponse(
            status=response.status_code,
            message=response.text,
            content=response.json()
        )
