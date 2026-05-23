
from fastapi import status, APIRouter, UploadFile, Depends
from core.ingestion_service.ingestion import IngestionService
from dependencies.service_clients import ServiceClients
from api.schemas.ingestion_schema import IngestResponse
from dependencies.yaml_extractor import YamlExtractor

class IngestionRouter:

    def __init__(self, extractor: YamlExtractor):
        self.__url_config = extractor.get_url_config()
        self.__ingestion_serv_config = extractor.get_ingestion_service_config()
        self.router = APIRouter(
            prefix=self.__ingestion_serv_config.endpoint,
            tags=[self.__ingestion_serv_config.tag]
        )
        # registering routes dynamically on init
        self.__register_routes()

    def __register_routes(self):
        self.router.add_api_route(
            path=self.__url_config.base_endpoint,
            endpoint=self._call_ingestion_service,
            methods=[self.__ingestion_serv_config.api_method],
            status_code=status.HTTP_201_CREATED,
            response_model=IngestResponse
        )

    async def _call_ingestion_service(
            self,
            uploaded_file: UploadFile,
            client=Depends(ServiceClients().get_ingestion_client)
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