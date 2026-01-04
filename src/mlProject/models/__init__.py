from pydantic import BaseModel
from typing import List
from pathlib import Path

class ReadYamlModel(BaseModel):
    file_path: Path

class CreateDirectoriesModel(BaseModel):
    directories: List[Path]
    verbose: bool = True

class SaveJsonModel(BaseModel):
    path: Path
    data: dict

class LoadJsonModel(BaseModel):
    path: Path   