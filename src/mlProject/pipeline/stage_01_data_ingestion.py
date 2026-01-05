from src.mlProject import logger
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_ingestion import DataIngestion
STAGE_NAME = "DATA_INGESTION_STAGE"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        cm = ConfigurationManager()
        data_ingestion_config = cm.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()