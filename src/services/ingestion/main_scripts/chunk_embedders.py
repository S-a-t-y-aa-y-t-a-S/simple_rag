from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from ingestion.utils.helpers import Helper


class ChunkEmbedder:
    def __init__(self, helper: Helper):
        self.__chunk_embedding_config = helper.get_embedder_config()
        self.__model_name = self.__chunk_embedding_config.embedding_model_name
        self.__embedding_function = HuggingFaceEmbeddings(model_name = self.__model_name)

    
    # def get_embedding_function(self):
    #     return self.__embedding_function


    def get_doc_content(self, document_chunks: list[Document]):
        return [doc_chunk.page_content for doc_chunk in document_chunks]


    def get_embeddings(self, document_chunks: list[Document]):
        doc_chunk_page_content = self.get_doc_content(document_chunks=document_chunks)
        return self.__embedding_function.embed_documents(texts=doc_chunk_page_content)
        