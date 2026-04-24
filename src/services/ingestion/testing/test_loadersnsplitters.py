from ingestion.main_scripts.loader_n_splitter.loaders import Loader
from ingestion.main_scripts.loader_n_splitter.splitters import Splitter
from ingestion.main_scripts.loader_n_splitter.merge_loader_splitters import LoaderNSplitter
from ingestion.utils.helpers import Helper


loader = Loader(helper=Helper())
splitter = Splitter(helper=Helper())
loader_n_splitter = LoaderNSplitter(loader=loader, splitter=splitter)

print(loader_n_splitter.run_loader_splitter())