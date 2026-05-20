from core.loader_n_splitter.loaders import Loader
from core.loader_n_splitter.splitters import Splitter
from core.storage.vector_stores import VectorStore
from dependencies.yaml_extractor import YamlExtractor
from api.schemas.ingestion_schema import IngestionResponse
from utils.file_processor import Processor
from utils.constants import Defaultvals

from fastapi import APIRouter, status, UploadFile, HTTPException
from typing import Optional
import os, tempfile, shutil


extractor = YamlExtractor()
api_config = extractor.get_api_config()
exception_config = extractor.get_exception_config()
return_config = extractor.get_return_config()
processor = Processor(default_bool_val=Defaultvals.DEFAULT_BOOL_VALUE)

ingest = APIRouter(
    prefix=api_config.endpoint,
    tags=[api_config.swagger_ui_tag]
)

loader = Loader(extractor=extractor)
splitter = Splitter(extractor=extractor)


@ingest.post(path=api_config.base_url, status_code=status.HTTP_201_CREATED, response_model=IngestionResponse)
async def ingest_doc(uploaded_file: UploadFile):

    
    await uploaded_file.seek(offset=Defaultvals.DEFAULT_INT_VALUE)
    file_path = processor.stage(uploaded_file=uploaded_file, exception_config=exception_config)

    if os.path.exists(file_path):
        # print(file_path)
        doc_loader = loader.pdf_loader(uploaded_file=file_path)
        doc_chunks = splitter.doc_splitter(documents=doc_loader)
        storage = VectorStore(extractor=extractor)
        storage.store_embeddings(doc_chunks=doc_chunks)

        os.remove(file_path)

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exception_config.file
        )
    
    return IngestionResponse(return_statement=return_config.ingestion)