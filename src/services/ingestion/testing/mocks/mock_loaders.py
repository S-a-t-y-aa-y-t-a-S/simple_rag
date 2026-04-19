
from ingestion.main_scripts.loader_n_splitter.loaders import Loader
from ingestion.utils.helpers import Helper


loader = Loader(helper=Helper())
print(loader.pdf_loader())


# previously calling LoaderConfig directly
# this time via Helper class for pydantic schema validation
# from constants import RAW_DATA_DIRECTORY
# loader = Loader(loader_config=LoaderConfig(filepath=constants.RAW_DATA_DIRECTORY))
# print(loader.pdf_loader())
