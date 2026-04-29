from ingestion.utils.helpers import Helper
from ingestion.src.chunk_embedders import ChunkEmbedder
from ingestion.src.loader_n_splitter.merge_loader_splitters import LoaderNSplitter
from ingestion.src.loader_n_splitter.loaders import Loader
from ingestion.src.loader_n_splitter.splitters import Splitter


helper = Helper()
loader = Loader(helper=helper)
splitter = Splitter(helper=helper)

chunk_embedder = ChunkEmbedder(helper=helper)
loader_n_splitter = LoaderNSplitter(loader=loader, splitter=splitter)

doc_chunks = loader_n_splitter.run_loader_splitter()
print(chunk_embedder.get_embeddings(document_chunks=doc_chunks))

