import json
from pathlib import Path
from typing import Self, Any, Generator

from untappr.checkin import CheckIn
from untappr.beer import Beer


class CheckIns:
    def __init__(self) -> None:
        self._entries: list[CheckIn] = []

    def add(self, entry: list[CheckIn] | CheckIn) -> None:
        if isinstance(entry, list):
            self._entries.extend(entry)
        else:
            self._entries.append(entry)

    def filter(self, beer: Beer | str | None) -> Generator[CheckIn, None, None]:
        if isinstance(beer, Beer):
            name = beer.name.lower()
        else:
            name = beer.lower()
        for checkin in self._entries:
            if name in checkin.beer.name.lower():
                yield checkin

    @classmethod
    def from_file(cls, file_path: Path) -> Self:
        return CheckIns.from_data(
            json.loads(file_path.read_text(encoding="utf-8"))
        )

    @classmethod
    def from_data(cls, data: list[dict[str, Any]]) -> Self:
        ret = cls()
        for entry in data:
            ret.add(CheckIn.from_data(entry))
        return ret

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(entries={len(self._entries)})"
