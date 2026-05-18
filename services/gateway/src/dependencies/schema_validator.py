from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from utils import constants
from pathlib import Path
import os

class Config(BaseSettings):
    yaml_file_path: str = Field(default_factory=str)
    