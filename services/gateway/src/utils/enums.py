
from enum import Enum


class Keys(Enum):
    INGESTION_PAYLOAD_KEY="uploaded_file"
    URL_KEY="url"
    SERVICE_COMMUNICATION_KEY="service_communication"


class DefaultValues(Enum):
    # default values
    EMPTY_STRING=""
    EMPTY_DICT={}
    EMPTY_LIST=[]
    NULL_VALUE=None
    DEFAULT_BOOL_VALUE=True
    DEFAULT_INT_VALUE=0