from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from collections.abc import Iterable
from dependencies.yaml_extractor import YamlExtractor


class Splitter:
    def __init__(self, extractor: YamlExtractor):
        self.__splitter_config = extractor.get_splitter_config()
        self.__chunksize = self.__splitter_config.chunksize
        self.__chunkoverlap = self.__splitter_config.chunkoverlap
        
    def doc_splitter(self, documents:Iterable[Document]):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.__chunksize,
            chunk_overlap=self.__chunkoverlap
        )
        return splitter.split_documents(documents=documents)
        