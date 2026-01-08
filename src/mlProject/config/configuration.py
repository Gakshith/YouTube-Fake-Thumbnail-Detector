from src.mlProject.utils.common import read_yaml, create_directories
from src.mlProject.constants import CONFIG_FILE_PATH, PARAM_FILE_PATH, SCHEMA_FILE_PATH
from src.mlProject.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, \
    ModelTrainerConfig, ModelEvaluationConfig
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

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([Path(config.root_dir)])
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_dir=config.data_path,
        )
        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.LogisticRegression
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )
        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.LogisticRegression
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri= "https://dagshub.com/Gakshith/YouTube-Fake-Thumbnail-Detector.mlflow"

        )

        return model_evaluation_config