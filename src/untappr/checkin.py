import dataclasses
import datetime
from typing import Any, Self

from untappr.beer import Beer


@dataclasses.dataclass
class CheckIn:
    id: int
    date: datetime.datetime
    beer: Beer
    comment: str
    rating: float
    serving_type: str
    photo_url: str
    venue: str

    @classmethod
    def from_data(cls, entry: dict[str, Any]) -> Self:
        return cls(
            id=entry["checkin_id"],
            date=datetime.datetime.strptime(entry["created_at"], r"%Y-%m-%d %H:%M:%S"),
            rating=entry["rating_score"],
            comment=entry["comment"],
            serving_type=entry["serving_type"],
            photo_url=entry["photo_url"],
            venue=entry["venue_name"],
            beer=Beer.from_data(entry)
        )

    @property
    def iso_datetime_str(self) -> str:
        return self.date.isoformat()

    @property
    def has_venue(self) -> bool:
        return bool(self.venue)

    def __str__(self) -> str:
        return (f"Checkin("
                f"date={self.date}, "
                f"beer={self.beer.name}, "
                f"brewery={self.beer.brewery.name}, "
                f"venue={self.venue or 'N/A'})"
                )

    def __repr__(self) -> str:
        return str(self)
