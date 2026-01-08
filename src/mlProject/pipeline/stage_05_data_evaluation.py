from src.mlProject.components.data_evaluation import ModelEvaluation
from src.mlProject.components.model_training import ModelTrainer
from src.mlProject.config.configuration import ConfigurationManager

STAGE_NAME ="Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
