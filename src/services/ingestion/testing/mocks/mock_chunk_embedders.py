from utils.helpers import Helper
from ingestion.main_scripts.chunk_embedders import ChunkEmbedder
from ingestion.main_scripts.loader_n_splitter.merge_loader_splitters import LoaderNSplitter
from ingestion.main_scripts.loader_n_splitter.loaders import Loader
from ingestion.main_scripts.loader_n_splitter.splitters import Splitter


helper = Helper()
loader = Loader(helper=helper)
splitter = Splitter(helper=helper)

chunk_embedder = ChunkEmbedder(helper=helper)
loader_n_splitter = LoaderNSplitter(loader=loader, splitter=splitter)

