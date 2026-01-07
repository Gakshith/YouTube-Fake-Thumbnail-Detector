from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation

STAGE_NAME = "DATA_VALIDATION_STAGE"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        cm = ConfigurationManager()
        dv_config = cm.get_data_validation_config()
        dv = DataValidation(config=dv_config)
        dv.validate_all_columns()
