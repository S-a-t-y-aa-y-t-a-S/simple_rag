class LoaderConfig:
    filepath: str

class SplitterConfig:
    chunksize: int
    chunkoverlap: int

class EmbedderConfig:
    model_name: str

class VectorStoreConfig:
    folder_dir: str
    collection_name: str

class LoggerConfig:
    pass