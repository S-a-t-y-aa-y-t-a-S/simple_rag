
from enum import Enum
from typing import Mapping, Any
from types import MappingProxyType


class ImmutableMetaClass(type):

    def __setattr__(cls, name: str, value: Any)-> None:
        raise AttributeError(
            f"Class '{cls.__name__}' is immutable. Cannot modify attribute '{name}'"
        )

    def __delattr__(cls, name: str, value: Any):
        raise AttributeError(
            f"Class '{cls.__name__}' is immutable. Cannot delete attribute '{name}'"
        )


class DefaultVals(metaclass=ImmutableMetaClass):
    EMPTY_STRING: str = ""
    EMPTY_TUPLE: tuple[()] = ()
    EMPTY_DICT: Mapping[Any, Any] = MappingProxyType({})
    NULL_TYPE = None
    DEFAULT_BOOL_VALUE: bool = True
    DEFAULT_INT_VALUE: int = 0


class ConfigKey(str, Enum):
    URL_CONFIG_KEY="url_config"
    SERVICE_COMM_CONFIG_KEY="service_comm_config"
    

class FileConfig(str, Enum):
    ENVIRONMENT_FILE="configs/.env"
    READ_FILE_MODE="r"