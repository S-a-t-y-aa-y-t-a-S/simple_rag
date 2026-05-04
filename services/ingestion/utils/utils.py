import fastapi
from configs import constants
import tempfile
import shutil, os
from configs.ingestion_configs import ExceptionConfig

def file_handling(uploaded_file: fastapi.UploadFile|str, exception_config: ExceptionConfig):
    
    try:
        file_path = str(os.path.join(tempfile.gettempdir(), uploaded_file.filename))

        with open(file=file_path,
                mode=constants.WRITE_FILE_MODE_BINARY) as buffer:
            shutil.copyfileobj(
                fsrc=uploaded_file.file,
                fdst=buffer
            )        
            return file_path

    except Exception as exp:
        print(exception_config.saving_file, exp)
        

        
        
