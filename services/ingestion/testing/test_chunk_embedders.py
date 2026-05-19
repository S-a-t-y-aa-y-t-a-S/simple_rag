from src.dependencies.yaml_extractor import YamlExtractor
from src.core.embedder.chunk_embedders import ChunkEmbedder
from src.core.loader_n_splitter.merge_loader_splitters import LoaderNSplitter
from src.core.loader_n_splitter.loaders import Loader
from src.core.loader_n_splitter.splitters import Splitter


extractor = YamlExtractor()
loader = Loader(extractor=extractor)
splitter = Splitter(extractor=extractor)

chunk_embedder = ChunkEmbedder(extractor=extractor)
loader_n_splitter = LoaderNSplitter(loader=loader, splitter=splitter)

doc_chunks = loader_n_splitter.run_loader_splitter()
print(chunk_embedder.get_embeddings(document_chunks=doc_chunks))

