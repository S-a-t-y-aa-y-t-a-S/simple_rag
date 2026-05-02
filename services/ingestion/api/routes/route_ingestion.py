from src.loader_n_splitter.loaders import Loader
from src.loader_n_splitter.splitters import Splitter
from src.vector_stores import VectorStore
from utils.helpers import Helper
from api.schemas.ingestion_schema import IngestionResponse

from fastapi import APIRouter, status, UploadFile, File

helper = Helper()
api_config = helper.get_api_config()

ingest = APIRouter(
    prefix=api_config.endpoint,
    tags=[api_config.swagger_ui_tag]
)

loader = Loader(helper=helper)
splitter = Splitter(helper=helper)


@ingest.post(path=api_config.base_url, status_code=status.HTTP_201_CREATED, response_model=IngestionResponse)
def ingest_doc(uploaded_file: UploadFile = File(...)):

    doc_loader = loader.pdf_loader(uploaded_file=uploaded_file)
    doc_chunks = splitter.doc_splitter(documents=doc_loader)
    storage = VectorStore(helper=helper)
    storage.store_embeddings(doc_chunks=doc_chunks)
    
    return api_config.return_statement