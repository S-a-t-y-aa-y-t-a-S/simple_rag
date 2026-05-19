from dependencies.yaml_extractor import YamlExtractor
from core.embedder.chunk_embedders import ChunkEmbedder
from langchain_chroma import Chroma
from langchain_core.documents import Document


class VectorStore (ChunkEmbedder):
    def __init__(self, extractor: YamlExtractor):

        super().__init__(extractor=YamlExtractor())

        self.__storage_config = extractor.get_storage_config()
        self.__folder_dir = self.__storage_config.folder_dir
        self.__collection_name = self.__storage_config.collection_name


    def store_embeddings(self, doc_chunks: list[Document])-> list[str]:
        vector_db = Chroma(
            collection_name=self.__collection_name,
            embedding_function=self._ChunkEmbedder__embedding_function,
            persist_directory=self.__folder_dir
        )
        vector_db.add_texts(
            texts=self.get_doc_content(document_chunks=doc_chunks),
            embeddings=self.get_embeddings(document_chunks=doc_chunks)        
        )