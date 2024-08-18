from src.TextSum.config.configuration import ConfigurationManager
from src.TextSum.components.data_transformation import DataTransformation
from src.TextSum.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
            config=ConfigurationManager()
            data_transformation_config=config.get_data_transformation()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()