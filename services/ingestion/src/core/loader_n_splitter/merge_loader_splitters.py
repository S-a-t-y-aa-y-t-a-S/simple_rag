from .loaders import Loader
from .splitters import Splitter
from langchain_core.documents import Document


class LoaderNSplitter:
    def __init__(self, loader: Loader, splitter: Splitter):
        self.loader = loader
        self.splitter = splitter
        

    def run_loader_splitter(self)-> list[Document]:
        document_list = self.loader.pdf_loader()
        document_chunks = self.splitter.doc_splitter(documents=document_list)
        return document_chunks