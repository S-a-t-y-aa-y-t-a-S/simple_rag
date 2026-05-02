from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from collections.abc import Iterable
from utils.helpers import Helper


class Splitter:
    def __init__(self, helper: Helper):
        self.__splitter_config = helper.get_splitter_config()
        self.__chunksize = self.__splitter_config.chunksize
        self.__chunkoverlap = self.__splitter_config.chunkoverlap
        
    def doc_splitter(self, documents:Iterable[Document]):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.__chunksize,
            chunk_overlap=self.__chunkoverlap
        )
        return splitter.split_documents(documents=documents)
        