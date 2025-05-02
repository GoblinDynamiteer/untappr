
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget

from untappr import CheckIns
from untappr.gui.check_ins_widget import CheckinsWidget


class MainWindow(QMainWindow):
    signal_got_exit_request = Signal()

    def __init__(self, check_ins: CheckIns):
        QMainWindow.__init__(self)
        self.setWindowTitle("Untappr")
        self._init(check_ins)

    def _init(self, check_ins: CheckIns):
        widget = QWidget()
        widget.setLayout(QVBoxLayout())
        btn = QPushButton("Exit")
        btn.clicked.connect(self.signal_got_exit_request)
        widget.layout().addWidget(CheckinsWidget(check_ins))
        widget.layout().addWidget(btn)
        self.setCentralWidget(widget)

