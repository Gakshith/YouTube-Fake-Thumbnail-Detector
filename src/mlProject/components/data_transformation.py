from src.mlProject.utils.common import create_directories
from src.mlProject.entity.config_entity import DataTransformationConfig
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from sklearn.pipeline import Pipeline
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        data_path = self.config.data_dir

        self.data = pd.read_csv(data_path)

        create_directories([self.config.root_dir])

        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def data_information(self):
        data_dtype_info = pd.DataFrame(self.data.dtypes).rename(columns={0: "DataType"})
        data_null_info = pd.DataFrame(self.data.isnull().sum()).rename(columns={0: "Null Value Count"})
        data_total_info = pd.concat([data_dtype_info, data_null_info], axis=1)
        return data_total_info

    def figure_1(self, data_total_info: pd.DataFrame):
        plt.figure(figsize=(8, 4))
        plt.title("Null Value Count")
        plt.xlabel("COLUMN NAMES")
        plt.ylabel("COUNT OF NULL VALUES")
        plt.ylim(bottom=0)
        plt.bar(x=data_total_info.index.astype(str), height=data_total_info["Null Value Count"].values)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def figure_2(self, df: pd.DataFrame):
        from collections import Counter

        def length_counter(series):
            counter = Counter()
            for text in series.fillna("").astype(str):
                l = len(text)
                if l < 20:
                    counter["Less Than 20"] += 1
                elif l < 30:
                    counter["Less Than 30"] += 1
                else:
                    counter["40 or More"] += 1
            return counter

        counts = length_counter(df["headline"])

        plt.figure(figsize=(7, 4))
        plt.title("Titles Classification Based On Length")
        plt.xlabel("CLASSIFICATION TYPE")
        plt.ylabel("COUNT")
        plt.ylim(bottom=0)
        plt.bar(list(counts.keys()), list(counts.values()))
        plt.tight_layout()
        plt.show()

    def data_preprocessing(self, text: str) -> str:
        if not isinstance(text, str) or not text.strip():
            return ""

        text = text.lower()
        text = re.sub(r"[^a-zA-Z\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()

        tokens = word_tokenize(text)
        tokens = [w for w in tokens if w not in self.stop_words and len(w) > 2]
        tokens = [self.lemmatizer.lemmatize(w) for w in tokens]

        return " ".join(tokens)

    def data_selection(self):
        data_information = self.data_information()
        self.figure_1(data_information)
        self.figure_2(self.data)

        df = self.data.copy()
        df["headline"] = df["headline"].fillna("").astype(str)
        df["headline"] = df["headline"].apply(self.data_preprocessing)

        X = df["headline"]
        y = df["clickbait"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        train_df = pd.DataFrame({"headline": X_train, "clickbait": y_train})
        test_df = pd.DataFrame({"headline": X_test, "clickbait": y_test})

        train_df.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_df.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        return train_df, test_df