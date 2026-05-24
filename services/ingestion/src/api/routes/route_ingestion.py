
from core.loader_n_splitter.loaders import Loader
from core.loader_n_splitter.splitters import Splitter
from core.storage.vector_stores import VectorStore
from dependencies.yaml_extractor import YamlExtractor
from api.schemas.ingestion_schema import IngestionResponse
from utils.file_processor import Processor
from utils.constants import Defaultvals

from fastapi import APIRouter, status, UploadFile, HTTPException
import os


class RouteIngestion:

    def __init__(self, extractor: YamlExtractor):
    
        self._extractor = extractor
        self._api_config = self._extractor.get_api_config()
        self._exception_config = self._extractor.get_exception_config()
        self._return_config = self._extractor.get_return_config()
        self._processor = Processor(
            default_bool_val=Defaultvals.DEFAULT_BOOL_VALUE
        )
        self.router = APIRouter(
            prefix=self._api_config.endpoint,
            tags=[self._api_config.swagger_ui_tag]
        )
        self._register_routes()


    def _register_routes(self):

        self.router.add_api_route(
            path=self._api_config.base_url,
            endpoint=self._ingest_doc,
            methods=[self._api_config.method],
            status_code=status.HTTP_201_CREATED,
            response_model=IngestionResponse
        )


    async def _ingest_doc(self,
                        uploaded_file: UploadFile):

        await uploaded_file.seek(offset=Defaultvals.DEFAULT_INT_VALUE)
        file_path = self._processor.stage(uploaded_file=uploaded_file, exception_config=self._exception_config)

        if os.path.exists(file_path):
            # print(file_path)
            doc_loader = Loader(extractor=self._extractor).pdf_loader(uploaded_file=file_path)
            doc_chunks = Splitter(extractor=self._extractor).doc_splitter(documents=doc_loader)
            storage = VectorStore(extractor=self._extractor)
            storage.store_embeddings(doc_chunks=doc_chunks)

            os.remove(file_path)

        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=self._exception_config.file
            )
        
        return IngestionResponse(return_statement=self._return_config.ingestion)