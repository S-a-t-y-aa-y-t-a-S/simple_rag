from configs import constants, ingestion_configs
import yaml

class Helper:

    def __init__(
            self,
            file_mode: str = constants.READ_FILE_MODE):
        
        self.ingestion_configuration = ingestion_configs.BasicConfig()
        self.yaml_file_path = self.ingestion_configuration.yaml_file_path
        self.file_mode = file_mode

        with open(file=self.yaml_file_path, mode=self.file_mode) as yaml_file:
            self.yaml_data = yaml.safe_load(yaml_file)


        
