import json
from pathlib import Path
from typing import Self, Any, Generator

from untappr.checkin import CheckIn
from untappr.beer import Beer


class CheckIns:
    def __init__(self) -> None:
        self._entries: list[CheckIn] = []

    @property
    def latest(self) -> CheckIn:
        return self.by_date[-1]

    @property
    def first(self) -> CheckIn:
        return self.by_date[0]

    @property
    def by_date(self) -> list[CheckIn]:
        return sorted(self._entries, key=lambda x: x.date)

    def add(self, entry: list[CheckIn] | CheckIn) -> None:
        if isinstance(entry, list):
            self._entries.extend(entry)
        else:
            self._entries.append(entry)

    def filter(self, pattern: str) -> Generator[CheckIn, None, None]:
        _matches: list[CheckIn] = []
        _funcs = [self.filter_beer,
                  self.filter_brewery,
                  self.filter_datetime,
                  self.filter_venue]
        for _func in _funcs:
            for match in list(_func(pattern)):
                if match not in _matches:
                    _matches.append(match)
        for entry in _matches:
            yield entry

    def filter_beer(self, beer: Beer | str | None) -> Generator[CheckIn, None, None]:
        if isinstance(beer, Beer):
            name = beer.name.lower()
        else:
            name = beer.lower()
        for checkin in self._entries:
            if name in checkin.beer.name.lower():
                yield checkin

    def filter_brewery(self, brewery_name: str | None) -> Generator[CheckIn, None, None]:
        for checkin in self._entries:
            if brewery_name.lower() in checkin.beer.brewery.name.lower():
                yield checkin

    def filter_datetime(self, datetime_str: str | None) -> Generator[CheckIn, None, None]:
        for checkin in self._entries:
            if datetime_str.lower() in checkin.iso_datetime_str.lower():
                yield checkin

    def filter_venue(self, venue: str | None) -> Generator[CheckIn, None, None]:
        for checkin in self._entries:
            if not checkin.has_venue:
                continue
            if venue.lower() in checkin.venue.lower():
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

    def __iter__(self):
        for check_in in self._entries:
            yield check_in
