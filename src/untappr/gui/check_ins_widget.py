from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel

from untappr import CheckIns
from untappr.gui.check_ins_tree import CheckInsTree


class CheckinsWidget(QWidget):
    def __init__(self, check_ins: CheckIns):
        QWidget.__init__(self)
        self._tree = CheckInsTree(check_ins)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self._tree)
        self.layout().addLayout(self._create_filter())

    def _create_filter(self) -> QHBoxLayout:
        edit = QLineEdit()
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Filter"))
        layout.addWidget(edit)

        def _changed(pattern: str):
            for item in self._tree:
                item.apply_filter(pattern)
            pass

        edit.textChanged.connect(_changed)
        return layout