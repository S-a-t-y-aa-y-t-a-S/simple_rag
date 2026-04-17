from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from collections import Iterable
from ingestion.configs.ingestion_configs import SplitterConfig


class Splitter:
    def __init__(self, splitter_config: SplitterConfig):
        self.__chunksize = splitter_config.chunksize
        self.__chunkoverlap = splitter_config.chunkoverlap
        
    def doc_splitter(self, documents:Iterable[Document]):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.__chunksize,
            chunk_overlap=self.__chunkoverlap
        )
        return splitter.split_documents(documents=documents)
        