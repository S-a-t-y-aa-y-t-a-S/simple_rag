from langchain_community.document_loaders import PyPDFLoader
from ingestion.utils.helpers import Helper


class Loader:
    def __init__(self, helper: Helper):
        self.__loader_config = helper.get_loader_config()
        self.__filepath = self.__loader_config.filepath
    
    def pdf_loader(self):
        loader = PyPDFLoader(file_path=self.__filepath)
        return loader.load()