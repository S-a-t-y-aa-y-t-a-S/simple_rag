
import httpx
from fastapi import UploadFile
from dependencies.yaml_extractor import YamlExtractor


class IngestionService:

    def __init__(self):
        self.__ingestion_serv_config = YamlExtractor().get_ingestion_service_config()

    async def forward_file(self,
                           uploaded_file: UploadFile,
                           client: httpx.AsyncClient)-> dict:
        
        file_content = await uploaded_file.read()

        payload = {
            self.__ingestion_serv_config.payload_key: (
                uploaded_file.filename,
                file_content,
                uploaded_file.content_type
            )
        }

        return await client.post(
            url=self.__ingestion_serv_config.endpoint,
            files=payload
        )
    