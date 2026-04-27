from ingestion.main_scripts.loader_n_splitter.loaders import Loader
from ingestion.main_scripts.loader_n_splitter.splitters import Splitter
from ingestion.main_scripts.vector_stores import VectorStore
from ingestion.utils.helpers import Helper
from . import constants

helper = Helper()


loader = Loader(helper=helper)
doc_loader = loader.pdf_loader()
print(f"loader {constants.SUCCESSFUL}")


splitter = Splitter(helper=helper)
doc_chunks = splitter.doc_splitter(documents=doc_loader)
print(f"splitter {constants.SUCCESSFUL}")


storage = VectorStore(helper=helper)
storage.store_embeddings(doc_chunks=doc_chunks)
print(f"Embedding and its storage {constants.SUCCESSFUL}")