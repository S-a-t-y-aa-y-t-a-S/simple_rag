from src.dependencies.yaml_extractor import YamlExtractor
from src.core.storage.vector_stores import VectorStore
from .. import utils, constants

from langchain_core.documents import Document
import json


vector_store = VectorStore(helper=Helper())

json_data = utils.file_handling(
    file_path=constants.DOC_CHUNKS_JSON_FILE,
    write_operation=not constants.DEFAULT_BOOL_VALUE,
    )

raw_string = json_data[constants.DOC_CHUNKS_KEY]
raw_json_value = json.loads(raw_string)
doc_chunks = [Document(**chunk) for chunk in raw_json_value] # unpacking is being done 

vector_store.store_embeddings(doc_chunks=doc_chunks)