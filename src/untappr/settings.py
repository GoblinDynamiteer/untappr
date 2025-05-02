import argparse
import dataclasses
import pathlib
from typing import Self


@dataclasses.dataclass
class Settings:
    file_path: pathlib.Path
    search_filter: str = ""

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
            parser.add_argument("--search", "-s",
                default="",
                dest="search",
                help="search checkins for brewery, beer, venue, date, ...")
            return parser.parse_args()

        args = _get_args()
        return cls(
            file_path=args.file_path,
            search_filter=args.search
        )
