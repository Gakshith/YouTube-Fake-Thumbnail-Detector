from src.mlProject.components.model_training import ModelTrainer
from src.mlProject.config.configuration import ConfigurationManager

STAGE_NAME ="Model Training Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
