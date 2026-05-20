
from enum import Enum
from typing import Mapping, Any
from types import MappingProxyType


class ImmutableMetaClass(type):
    '''prevents the child class attributes
    from being modified'''
    def __setattr__(cls, name: str, value: Any) -> None:
        raise AttributeError(
            f"Class '{cls.__name__}' is immutable. Cannot modify attribute '{name}'."
        )

    def __delattr__(cls, name: str) -> None:
        raise AttributeError(
            f"Class '{cls.__name__}' is immuatable. Connot delete attribute '{name}'."
        )


# default values
class Defaultvals(metaclass=ImmutableMetaClass):
    EMPTY_STRING: str = ""
    EMPTY_TUPLE: tuple[()] = () # since list is mutable, we shall use type casting 
    # in that case
    EMPTY_DICT: Mapping[Any, Any] = MappingProxyType({})
    NULL_VALUE = None # only works for None, no explicit mentioning of ClassVar, treated as 
    # static implicitly
    DEFAULT_BOOL_VALUE: bool = True
    DEFAULT_INT_VALUE: int = 0


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


