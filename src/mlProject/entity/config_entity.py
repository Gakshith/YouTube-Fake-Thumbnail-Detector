from dataclasses import dataclass
from pathlib import Path
from typing import Dict


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data: Path
    validation_status_file: Path
    all_schema: Dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir:Path
    data_dir:Path