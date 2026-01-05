from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

@dataclass(frozen=True)
class ReadYamlModel:
    file_path: Path

    def __post_init__(self) -> None:
        if not isinstance(self.file_path, Path):
            raise TypeError("file_path must be a pathlib.Path")


@dataclass(frozen=True)
class CreateDirectoriesModel:
    directories: List[Path]
    verbose: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.directories, list):
            raise TypeError("directories must be a list of pathlib.Path values")
        if not all(isinstance(item, Path) for item in self.directories):
            raise TypeError("directories must only contain pathlib.Path values")


@dataclass(frozen=True)
class SaveJsonModel:
    path: Path
    data: Dict[str, Any]

    def __post_init__(self) -> None:
        if not isinstance(self.path, Path):
            raise TypeError("path must be a pathlib.Path")
        if not isinstance(self.data, dict):
            raise TypeError("data must be a dict")


@dataclass(frozen=True)
class LoadJsonModel:
    path: Path

    def __post_init__(self) -> None:
        if not isinstance(self.path, Path):
            raise TypeError("path must be a pathlib.Path")
