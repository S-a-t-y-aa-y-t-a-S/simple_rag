from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from . import constants
from pathlib import Path
import os

class BasicConfig(BaseSettings):
    # extracting out the keys from .env file
    yaml_file_path:str = Field(default_factory=str)

    # obtaining the .env file path using Config class 
    model_config = SettingsConfigDict(
        env_file = os.path.join(Path(__file__).resolve().parent, constants.ENVIRONMENT_FILE)
    )
    

class LoaderConfig(BaseModel):
    filepath: str

class SplitterConfig(BaseModel):
    chunksize: int
    chunkoverlap: int

# class EmbedderConfig(BaseModel):
#     model_name: str

# class VectorStoreConfig(BaseModel):
#     folder_dir: str
#     collection_name: str

# class LoggerConfig:
#     pass