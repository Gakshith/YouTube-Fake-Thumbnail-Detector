from src.mlProject.components.data_transformation import DataTransformation
from src.mlProject.config.configuration import ConfigurationManager


STAGE_NAME = "DATA_TRANSFORMATION_STAGE"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.data_information()
        data_transformation.data_selection()
