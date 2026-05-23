
from utils.constants import FileConfig, DefaultVals, ConfigKey
from dependencies import schema_validator
import yaml

class YamlExtractor:

    def __init__(
        self,
        file_mode: str = FileConfig.READ_FILE_MODE
    ):

        self.gateway_configuration = schema_validator.Config()
        self.yaml_file_path = self.gateway_configuration.yaml_file_path
        self.file_mode = file_mode
        
        with open(file=self.yaml_file_path, mode=self.file_mode) as yaml_file:
            self.yaml_data = yaml.safe_load(yaml_file)
        
    
    def load_section(self,
                    section_name: str,
                    section_class):
        section = self.yaml_data.get(section_name, DefaultVals.EMPTY_DICT)
        return section_class(**section)

    
    def get_url_config(self):
        return self.load_section(
            section_name=ConfigKey.URL_CONFIG_KEY,
            section_class=schema_validator.URLConfig
        )

    def get_ingestion_service_config(self):
        return self.load_section(
            section_name=ConfigKey.INGESTION_SERVICE_CONFIG_KEY,
            section_class=schema_validator.IngestionServiceConfig
        )

    def get_service_comm_config(self):
        return self.load_section(
            section_name=ConfigKey.SERVICE_COMM_CONFIG_KEY,
            section_class=schema_validator.ServiceCommConfig
        )