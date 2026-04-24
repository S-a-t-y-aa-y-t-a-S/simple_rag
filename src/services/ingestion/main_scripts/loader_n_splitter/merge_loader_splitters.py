from .loaders import Loader
from .splitters import Splitter

class LoaderNSplitter:
    def __init__(self, loader: Loader, splitter: Splitter):
        self.loader = loader
        self.splitter = splitter
        

    def run_loader_splitter(self):
        document_list = self.loader.pdf_loader()
        document_chunks = self.splitter.doc_splitter(documents=document_list)
        return document_chunks