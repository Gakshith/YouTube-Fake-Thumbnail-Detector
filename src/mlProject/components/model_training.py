from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from src.mlProject.entity.config_entity import ModelTrainerConfig
from sklearn.pipeline import Pipeline
import os
import pickle as pkl
import pandas as pd

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        X_train = train_data["headline"].astype(str)
        y_train = train_data[self.config.target_column]

        model = LogisticRegression(
            l1_ratio=self.config.l1_ratio,
            random_state=42,
            solver='saga',
            max_iter=1000
        )
        pipe = Pipeline([
            ("vectorizer",TfidfVectorizer(ngram_range=(1,2),stop_words='english')),
            ("model",model)
        ])

        pipe.fit(X_train,y_train)
        with open(os.path.join(self.config.root_dir, self.config.model_name), "wb") as f:
              pkl.dump(pipe, f)