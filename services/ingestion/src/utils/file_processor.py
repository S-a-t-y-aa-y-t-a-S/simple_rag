import fastapi
from .constants import Defaultvals
import tempfile
import shutil, os
from dependencies.schema_validator import ExceptionConfig


class Processor:

    def __init__(self, default_bool_val: bool):
        self.__default_bool_val: bool = default_bool_val

    def stage(self, uploaded_file: fastapi.UploadFile|str, exception_config: ExceptionConfig):
        
        try:
            with tempfile.NamedTemporaryFile(
                delete=not self.__default_bool_val, # False
                suffix=f"_{uploaded_file.filename}"
            ) as temp_file:

                shutil.copyfileobj(uploaded_file.file, temp_file)
                file_path = temp_file.name      
            
            return file_path

        except Exception as exp:
            print(exception_config.saving_file, exp)
        

        
        
