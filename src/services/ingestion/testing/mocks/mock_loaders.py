
from ingestion.main_scripts.loader_n_splitter.loaders import Loader
from configs.ingestion_configs import LoaderConfig
# from constants import RAW_DATA_DIRECTORY

loader = Loader(loader_config=LoaderConfig)
print(loader.pdf_loader())
