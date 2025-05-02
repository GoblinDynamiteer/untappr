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