from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from collections.abc import Iterable
from dependencies.yaml_extractor import YamlExtractor
from utils import constants


class Loader:
    def __init__(self, extractor: YamlExtractor):
        self.__loader_config = extractor.get_loader_config()
        self.__filepath = self.__loader_config.filepath
    
    def pdf_loader(self, uploaded_file: str = constants.EMPTY_STRING)-> Iterable[Document]:
        if uploaded_file != constants.EMPTY_STRING:
            self.__filepath
            
        loader = PyPDFLoader(file_path=self.__filepath)
        return loader.load()