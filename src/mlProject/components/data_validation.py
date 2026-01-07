import pandas as pd
from src.mlProject.entity.config_entity import (DataValidationConfig)

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            self.config.validation_status_file.parent.mkdir(parents=True, exist_ok=True)

            data = pd.read_csv(self.config.unzip_data)
            data_cols = set(data.columns)

            validation_status = True if "headline" in data_cols else False

            with open(self.config.validation_status_file, "w") as f:
                f.write(f"DATA_VALIDATION_STATUS: {validation_status}\n")

            return validation_status

        except Exception as e:
            raise e