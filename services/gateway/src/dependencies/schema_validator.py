from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from utils.constants import FileConfig
from pathlib import Path
import os

class Config(BaseSettings):
    # extracting out the keys from .env file
    yaml_file_path: str = Field(default_factory=str)

    #obtaining the .env file path using Config class
    model_config = SettingsConfigDict(
        env_file = os.path.join(Path(__file__).resolve().parent.parent.parent, FileConfig.ENVIRONMENT_FILE)
    )

class URLConfig(BaseModel):
    host: str
    port: int
    endpoint: str
    

class ServiceCommConfig(BaseModel):
    timeout: int
    