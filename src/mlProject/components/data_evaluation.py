from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error,r2_score
import pickle
import dagshub
import pandas as pd
import numpy as np
from pathlib import Path
from src.mlProject.entity.config_entity import ModelEvaluationConfig
from src.mlProject.utils.common import save_json

dagshub.init(repo_owner='Gakshith', repo_name='YouTube-Fake-Thumbnail-Detector', mlflow=True)

import mlflow

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config


    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    def log_into_mlflow(self):
          test_data = pd.read_csv(self.config.test_data_path)
          with open(self.config.model_path, "rb") as file:
               model = pickle.load(file)
          X_test = test_data["headline"].astype(str)
          y_test = test_data[self.config.target_column].values.ravel()
          mlflow.set_tracking_uri(self.config.mlflow_uri)

          with mlflow.start_run():
               y_pred = model.predict(X_test)
               (rmse, mae, r2) = self.eval_metrics(y_test, y_pred)
               scores = {"rmse": rmse, "mae": mae, "r2": r2}
               save_json(path=Path(self.config.metric_file_name), data=scores)
               accuracy = accuracy_score(y_test, y_pred)
               # mlflow.log_params(self.config.all_params)
               mlflow.log_metric("rmse", rmse)
               mlflow.log_metric("r2", r2)
               mlflow.log_metric("mae", mae)
               mlflow.sklearn.log_model(model, "model")