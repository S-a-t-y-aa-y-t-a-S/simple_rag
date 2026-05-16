import fastapi
from config import constants
import tempfile
import shutil, os
from dependencies.ingestion_configs import ExceptionConfig

def file_handling(uploaded_file: fastapi.UploadFile|str, exception_config: ExceptionConfig):
    
    try:
        with tempfile.NamedTemporaryFile(
            delete=not constants.DEFAULT_BOOL_VALUE, 
            suffix=f"_{uploaded_file.filename}"
        ) as temp_file:

            shutil.copyfileobj(uploaded_file.file, temp_file)
            file_path = temp_file.name      
        
        return file_path

    except Exception as exp:
        print(exception_config.saving_file, exp)
        

        
        
