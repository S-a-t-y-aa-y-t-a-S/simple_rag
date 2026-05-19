from src.core.loader_n_splitter.loaders import Loader
from src.core.loader_n_splitter.splitters import Splitter
from src.core.loader_n_splitter.merge_loader_splitters import LoaderNSplitter
from src.dependencies.yaml_extractor import YamlExtractor
from . import constants
import json


loader = Loader(extractor=YamlExtractor())
splitter = Splitter(extractor=YamlExtractor())
loader_n_splitter = LoaderNSplitter(loader=loader, splitter=splitter)

serializable_doc_chunks = [chunk.model_dump() for chunk in loader_n_splitter.run_loader_splitter()]

with open(file=constants.DOC_CHUNKS_JSON_FILE, mode=constants.WRITE_FILE_MODE) as json_file_ptr:
    json.dump({constants.DOC_CHUNKS_KEY: json.dumps(serializable_doc_chunks)}, json_file_ptr)

# print(loader_n_splitter.run_loader_splitter())