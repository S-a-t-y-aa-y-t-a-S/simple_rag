
from src.core.loader_n_splitter.loaders import Loader
from src.dependencies.yaml_extractor import YamlExtractor


loader = Loader(extractor=YamlExtractor())
print(loader.pdf_loader())


# previously calling LoaderConfig directly
# this time via Helper class for pydantic schema validation
# from constants import RAW_DATA_DIRECTORY
# loader = Loader(loader_config=LoaderConfig(filepath=constants.RAW_DATA_DIRECTORY))
# print(loader.pdf_loader())
