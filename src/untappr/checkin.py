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

    @classmethod
    def from_data(cls, entry: dict[str, Any]) -> Self:
        return cls(
            id=entry["checkin_id"],
            date=datetime.datetime.strptime(entry["created_at"], r"%Y-%m-%d %H:%M:%S"),
            rating=entry["rating_score"],
            comment=entry["comment"],
            serving_type=entry["serving_type"],
            photo_url=entry["photo_url"],
            beer=Beer.from_data(entry)

        )