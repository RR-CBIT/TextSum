from src.TextSum.config.configuration import ConfigurationManager
from src.TextSum.components.data_validation import DataValidation
from src.TextSum.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
            config= ConfigurationManager()
            data_validation_config=config.get_data_validation_config()
            data_validation= DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exist()