from ingestion.utils.helpers import Helper
# from ingestion.main_scripts.chunk_embedders import ChunkEmbedder
from langchain_core.documents import Document
from .. import constants
import json


helper = Helper()

# chunk_embedder = ChunkEmbedder(helper=helper)


with open(file=constants.DOC_CHUNKS_JSON_FILE, mode=constants.READ_FILE_MODE) as json_file_ptr:
    json_data = json.load(fp=json_file_ptr) # extracted the complete content (key-value) from json file


raw_string = json_data[constants.DOC_CHUNKS_KEY] # obtained the raw string using the key
raw_json_value = json.loads(raw_string) # de-serialization is done obtaining basic python data-structure
# in this case, it is list

doc_chunks = [Document(**chunk) for chunk in raw_string]

print(doc_chunks)

# with open(file=constants.DOC_EMBEDDING_JSON_FILE, mode=constants.WRITE_FILE_MODE) as json_file_ptr:
#     json.dump({constants.EMBEDDING_KEY: f"{chunk_embedder.get_embeddings(document_chunks=doc_chunks)}"}, json_file_ptr)


# print(chunk_embedder.get_embeddings(document_chunks=doc_chunks))

