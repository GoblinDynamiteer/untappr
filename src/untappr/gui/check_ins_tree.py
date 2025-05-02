from PySide6.QtWidgets import QTreeWidget

from untappr import CheckIns
from untappr.gui.check_in_tree_item import CheckInTreeItem
from untappr.gui.enums import CheckInTreeColumns


class CheckInsTree(QTreeWidget):
    def __init__(self, check_ins: CheckIns):
        self._check_ins = check_ins
        QTreeWidget.__init__(self)
        self.setHeaderLabels(CheckInTreeColumns.header_names())
        for check_in in self._check_ins:
            self.addTopLevelItem(CheckInTreeItem(check_in))