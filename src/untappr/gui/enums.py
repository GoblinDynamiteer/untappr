from enum import IntEnum


class CheckInTreeColumns(IntEnum):
    Date = 0
    Brewery = 1
    Beer = 2
    Venue = 3

    @staticmethod
    def header_names() -> list[str]:
        return [c.name for c in CheckInTreeColumns]
