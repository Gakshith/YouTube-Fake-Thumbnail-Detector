from src.mlProject.utils.common import read_yaml, create_directories
from src.mlProject.constants import CONFIG_FILE_PATH, PARAM_FILE_PATH, SCHEMA_FILE_PATH
from src.mlProject.entity.config_entity import DataIngestionConfig,DataValidationConfig
from pathlib import Path

class ConfigurationManager:
    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAM_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        create_directories([Path(self.config.artifacts_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        root_dir = Path(config.root_dir)
        create_directories([root_dir])

        return DataIngestionConfig(
            root_dir=root_dir,
            source_url=str(config.source_url),
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir),
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        create_directories([Path(self.config.artifacts_root)])
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([Path(config.root_dir)])

        return DataValidationConfig(
            root_dir=Path(config.root_dir),
            unzip_data=Path(config.unzip_data),
            validation_status_file=Path(config.Data_Validation_Status),
            all_schema=schema,
        )
