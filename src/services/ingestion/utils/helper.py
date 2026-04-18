from ingestion.configs import constants, ingestion_configs
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

    def load_section(self,
                     section_name: str,
                     section_class):
        section = self.yaml_data.get(section_name, constants.EMPTY_DICT)
        # empty dict is used as a fallback if the specific key is not present (section_name)
        return section_class(**section) # for schema validation, unpacking of the key-values
    # is done which extracted from yaml_data

    def get_loader_config(self):
        return self.load_section(
            section_name=constants.LOADER_CONFIG_KEY,
            section_class=ingestion_configs.LoaderConfig
        )
    
    def get_splitter_config(self):
        return self.load_section(
            section_name=constants.SPLITTER_CONFIG_KEY,
            section_class=ingestion_configs.SplitterConfig
        )



        
