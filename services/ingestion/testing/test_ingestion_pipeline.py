from src.core.loader_n_splitter.loaders import Loader
from src.core.loader_n_splitter.splitters import Splitter
from src.core.storage.vector_stores import VectorStore
from src.dependencies.yaml_extractor import YamlExtractor
from . import constants

extractor = YamlExtractor()


loader = Loader(extractor=extractor)
doc_loader = loader.pdf_loader()
print(f"loader {constants.SUCCESSFUL}")


splitter = Splitter(extractor=extractor)
doc_chunks = splitter.doc_splitter(documents=doc_loader)
print(f"splitter {constants.SUCCESSFUL}")


storage = VectorStore(extractor=extractor)
storage.store_embeddings(doc_chunks=doc_chunks)
print(f"Embedding and its storage {constants.SUCCESSFUL}")