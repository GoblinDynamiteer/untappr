from PySide6.QtWidgets import QWidget, QVBoxLayout

from untappr import CheckIns
from untappr.gui.check_ins_tree import CheckInsTree


class CheckinsWidget(QWidget):
    def __init__(self, check_ins: CheckIns):
        QWidget.__init__(self)
        self._tree = CheckInsTree(check_ins)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self._tree)
