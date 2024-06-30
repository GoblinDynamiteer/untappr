import dataclasses
from typing import Any, Self


@dataclasses.dataclass
class Brewery:
    name: str
    url: str
    country: str
    state: str
    id: int

    @classmethod
    def from_data(cls, entry: dict[str, Any]) -> Self:
        return cls(
            name=entry["brewery_name"],
            url=entry["brewery_url"],
            country=entry["brewery_country"],
            state=entry["brewery_state"],
            id=entry["brewery_id"]
        )
