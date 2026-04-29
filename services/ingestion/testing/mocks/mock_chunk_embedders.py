from ingestion.utils.helpers import Helper
from ingestion.src.chunk_embedders import ChunkEmbedder
from langchain_core.documents import Document
from .. import constants, utils
import json


helper = Helper()

chunk_embedder = ChunkEmbedder(helper=helper)

with open(file=constants.DOC_CHUNKS_JSON_FILE, mode=constants.READ_FILE_MODE) as json_file_ptr:
    json_data = json.load(fp=json_file_ptr) # extracted the complete content (key-value) from json file


json_data = utils.file_handling(file_path=constants.DOC_CHUNKS_JSON_FILE, 
                                write_operation=not constants.DEFAULT_BOOL_VALUE)


raw_string = json_data[constants.DOC_CHUNKS_KEY] # obtained the raw string using the key
raw_json_value = json.loads(raw_string) # de-serialization is done obtaining basic python data-structure
# in this case, it is list

doc_chunks = [Document(**chunk) for chunk in raw_json_value]

utils.file_handling(file_path=constants.DOC_EMBEDDING_JSON_FILE, 
                    json_dumps_content=chunk_embedder.get_embeddings(document_chunks=doc_chunks))




# print(chunk_embedder.get_embeddings(document_chunks=doc_chunks))

