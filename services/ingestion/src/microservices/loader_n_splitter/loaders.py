from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from collections.abc import Iterable
from utils.helpers import Helper
from configs import constants


class Loader:
    def __init__(self, helper: Helper):
        self.__loader_config = helper.get_loader_config()
        self.__filepath = self.__loader_config.filepath
    
    def pdf_loader(self, uploaded_file: str = constants.EMPTY_STRING)-> Iterable[Document]:
        if uploaded_file != constants.EMPTY_STRING:
            self.__filepath
            
        loader = PyPDFLoader(file_path=self.__filepath)
        return loader.load()