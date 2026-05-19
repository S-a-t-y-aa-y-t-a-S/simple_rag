
from src.core.loader_n_splitter.splitters import Splitter
from src.dependencies.yaml_extractor import YamlExtractor
from .. import constants

splitter = Splitter(
    extractor=YamlExtractor()
)
print(splitter.doc_splitter(documents=constants.SAMPLE_DOCUMENT))