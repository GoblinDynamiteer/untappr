import sys

from PySide6.QtWidgets import QApplication

from untappr import CheckIns
from untappr.gui.main import MainWindow


class Gui:
    def __init__(self, check_ins: CheckIns):
        self._app = QApplication()
        self._win = MainWindow(check_ins)
        self._win.signal_got_exit_request.connect(self._app.exit)

    def run(self):
        self._win.show()
        sys.exit(self._app.exec())
