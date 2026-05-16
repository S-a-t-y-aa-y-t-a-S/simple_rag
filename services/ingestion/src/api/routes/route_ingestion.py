from microservices.loader_n_splitter.loaders import Loader
from microservices.loader_n_splitter.splitters import Splitter
from microservices.storage.vector_stores import VectorStore
from dependencies.helpers import Helper
from api.schemas.ingestion_schema import IngestionResponse
from utils import file_handling
from fastapi import APIRouter, status, UploadFile, HTTPException
from typing import Optional
import os, tempfile, shutil

helper = Helper()
api_config = helper.get_api_config()
exception_config = helper.get_exception_config()
return_config = helper.get_return_config()

ingest = APIRouter(
    prefix=api_config.endpoint,
    tags=[api_config.swagger_ui_tag]
)

loader = Loader(helper=helper)
splitter = Splitter(helper=helper)


@ingest.post(path=api_config.base_url, status_code=status.HTTP_201_CREATED, response_model=IngestionResponse)
async def ingest_doc(uploaded_file: UploadFile):

    # file_path = file_handling(uploaded_file=uploaded_file, exception_config=exception_config)
    await uploaded_file.seek(offset=0)

    with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{uploaded_file.filename}") as temp_file:
        shutil.copyfileobj(uploaded_file.file, temp_file)
        file_path = temp_file.name

    if os.path.exists(file_path):
        print(file_path)
        doc_loader = loader.pdf_loader(uploaded_file=file_path)
        doc_chunks = splitter.doc_splitter(documents=doc_loader)
        storage = VectorStore(helper=helper)
        storage.store_embeddings(doc_chunks=doc_chunks)

        os.remove(file_path)

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exception_config.file
        )
    
    return IngestionResponse(return_statement=return_config.ingestion)