from PySide6.QtWidgets import QTreeWidgetItem

from untappr.checkin import CheckIn
from untappr.gui.enums import CheckInTreeColumns

class CheckInTreeItem(QTreeWidgetItem):
    def __init__(self, check_in: CheckIn):
        self._check_in = check_in
        QTreeWidgetItem.__init__(self)
        self.setText(CheckInTreeColumns.Date, str(self._check_in.date))
        self.setText(CheckInTreeColumns.Brewery, self._check_in.beer.brewery.name)
        self.setText(CheckInTreeColumns.Beer, self._check_in.beer.name)
        self.setText(CheckInTreeColumns.Venue, str(self._check_in.venue))

    def apply_filter(self, pattern: str):
        show = False
        if pattern.lower() in self._check_in.beer.name.lower():
            show = True
        if show or pattern.lower() in self._check_in.iso_datetime_str.lower():
            show = True
        if self._check_in.has_venue:
            if show or pattern.lower() in self._check_in.venue.lower():
                show = True
        if show or pattern.lower() in self._check_in.beer.brewery.name.lower():
            show = True
        self.setHidden(not show)