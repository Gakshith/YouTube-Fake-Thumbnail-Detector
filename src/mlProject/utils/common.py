import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from src.mlProject import logger
from typing import Any
from .models import ReadYamlModel, CreateDirectoriesModel, SaveJsonModel, LoadJsonModel


@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    try:
        ReadYamlModel(file_path=file_path)
        with open(file_path, 'r') as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file -> {file_path} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error loading YAML file {file_path}: {e}")
        raise

@ensure_annotations
def create_directories(path_of_directory: List[Path], verbose: bool = True):
    try:
        CreateDirectoriesModel(directories=path_of_directory, verbose=verbose)
        for path in path_of_directory:
            path.mkdir(parents=True, exist_ok=True)
            if verbose:
                logger.info(f"Created directory: {path}")
    except Exception as e:
        logger.error(f"Error creating directories: {e}")
        raise

@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        SaveJsonModel(path=path, data=data)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"json file saved at: {path}")
    except Exception as e:
        logger.error(f"Error saving JSON file {path}: {e}")
        raise

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        LoadJsonModel(path=path)
        with open(path, 'r') as f:
            content = json.load(f)
        logger.info(f"json file loaded successfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error loading JSON file {path}: {e}")
        raise

@ensure_annotations
def save_bin(data: Any, path: Path):
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"binary file saved at: {path}")
    except Exception as e:
        logger.error(f"Error saving binary file {path}: {e}")
        raise

@ensure_annotations
def load_bin(path: Path) -> Any:
    try:
        data = joblib.load(path)
        logger.info(f"binary file loaded from: {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading binary file {path}: {e}")
        raise

@ensure_annotations
def get_size(path: Path) -> str:
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)
        logger.info(f"Size of {path}: {size_in_kb} KB")
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logger.error(f"Error getting size of {path}: {e}")
        raise   