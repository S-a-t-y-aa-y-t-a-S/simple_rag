from ingestion.main_scripts.loader_n_splitter.loaders import Loader
from ingestion.main_scripts.loader_n_splitter.splitters import Splitter
from ingestion.main_scripts.loader_n_splitter.merge_loader_splitters import LoaderNSplitter
from ingestion.utils.helpers import Helper
from . import constants
import json


loader = Loader(helper=Helper())
splitter = Splitter(helper=Helper())
loader_n_splitter = LoaderNSplitter(loader=loader, splitter=splitter)


with open(file=constants.DOC_CHUNKS_JSON_FILE, mode=constants.WRITE_FILE_MODE) as json_file_ptr:
    json.dump({constants.DOC_CHUNKS_KEY: json.dumps(loader_n_splitter.run_loader_splitter())}, json_file_ptr)

# print(loader_n_splitter.run_loader_splitter())