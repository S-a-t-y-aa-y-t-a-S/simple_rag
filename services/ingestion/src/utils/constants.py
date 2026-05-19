from enum import Enum
from typing import ClassVar, Final, Mapping, Any


# default values
class Defaultvals:
    EMPTY_STRING: Final[ClassVar[str]]=""
    EMPTY_TUPLE: Final[ClassVar[tuple[()]]] = () # since list is mutable, we shall use type casting 
    # in that case
    EMPTY_DICT: Final[ClassVar[Mapping[Any, Any]]] = {}
    NULL_VALUE: Final=None # only works for None, no explicit mentioning of ClassVar, treated as 
    # static implicitly
    DEFAULT_BOOL_VALUE: Final[ClassVar[bool]]=True
    DEFAULT_INT_VALUE: Final[ClassVar[int]]=0


# keys present in yaml
class ConfigKey(str, Enum):
    LOADER_CONFIG_KEY="loader_config"
    SPLITTER_CONFIG_KEY="splitter_config"
    EMBEDDER_CONFIG_KEY="chunk_embedder_config"
    STORAGE_CONFIG_KEY="vector_store_config"
    LOGGER_CONFIG_KEY="logger_config"
    API_CONFIG_KEY="api_config"
    RETURN_CONFIG_KEY="return_config"
    EXCEPTION_CONFIG_KEY="exception_config"


# file configurations amd extensions
class FileConfig(str, Enum):
    ENVIRONMENT_FILE="configs/.env"
    READ_FILE_MODE="r"
    WRITE_FILE_MODE_BINARY="wb"
    PDF_EXT=".pdf"


