import dataclasses
from typing import Any, Self

from untappr.brewery import Brewery


@dataclasses.dataclass
class Beer:
    brewery: Brewery
    name: str
    type: str
    abv: float
    ibu: int
    url: str

    @classmethod
    def from_data(cls, entry: dict[str, Any]) -> Self:
        return cls(
            name=entry["beer_name"],
            type=entry["beer_type"],
            abv=entry["beer_abv"],
            ibu=entry["beer_ibu"],
            url=entry["beer_url"],
            brewery=Brewery.from_data(entry)
        )
