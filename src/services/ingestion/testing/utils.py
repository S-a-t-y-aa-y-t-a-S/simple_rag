import json
from . import constants
from typing import Any

def file_handling(file_path: str, write_operation: bool = constants.DEFAULT_BOOL_VALUE, json_dumps_content: None|Any = constants.NULL_VALUE)-> None|Any:
    
    json_data = constants.NULL_VALUE

    if not write_operation:
        with open(file=file_path, mode=constants.READ_FILE_MODE) as json_file_ptr:
            json_data = json.load(fp=json_file_ptr) # extracted the complete content (key-value) from json file
    
    else:
        with open(file=file_path, mode=constants.WRITE_FILE_MODE) as json_file_ptr:
            json.dump({constants.EMBEDDING_KEY: json.dumps(json_dumps_content)}, json_file_ptr)

    return json_data