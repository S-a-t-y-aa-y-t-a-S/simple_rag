from langchain_community.document_loaders import PyPDFLoader
from ingestion.configs.ingestion_configs import LoaderConfig

class Loader:
    def __init__(self, loader_config: LoaderConfig):
        self.__filepath = loader_config.filepath
    
    def pdf_loader(self):
        loader = PyPDFLoader(file_path=self.__filepath)
        return loader.load()