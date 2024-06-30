import argparse
import dataclasses
import pathlib
from typing import Self


@dataclasses.dataclass
class Settings:
    file_path: pathlib.Path

    def __post_init__(self) -> None:
        if not self.file_path.is_file():
            raise FileNotFoundError(f"{self.file_path} is not a valid file!")

    @classmethod
    def create_from_args(cls) -> Self:
        def _get_args() -> argparse.Namespace:
            parser = argparse.ArgumentParser()
            parser.add_argument(
                "--file", "-f",
                dest="file_path",
                help="Path to JSON export.",
                type=pathlib.Path)
            return parser.parse_args()

        return cls(file_path=_get_args().file_path)
