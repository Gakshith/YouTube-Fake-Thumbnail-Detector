import zipfile
from pathlib import Path
from src.mlProject import logger
from src.mlProject.utils.common import get_size
import ssl
import certifi
from src.mlProject.entity.config_entity import (DataIngestionConfig)
import urllib.request as request

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
         if not self.config.local_data_file.exists():
              self.config.local_data_file.parent.mkdir(parents=True, exist_ok=True)
              ctx = ssl.create_default_context(cafile=certifi.where())

              with request.urlopen(self.config.source_url, context=ctx) as r, open(self.config.local_data_file, "wb") as f:
                 f.write(r.read())

              logger.info(f"Downloaded file to: {self.config.local_data_file}")
         else:
             logger.info(f"File already exists of size: {get_size(self.config.local_data_file)}")

    def extract_zip_file(self):
        self.config.unzip_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)