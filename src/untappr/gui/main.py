
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget


class MainWindow(QMainWindow):
    signal_got_exit_request = Signal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Untappr")
        self._init()

    def _init(self):
        widget = QWidget()
        widget.setLayout(QVBoxLayout())
        btn = QPushButton("Exit")
        btn.clicked.connect(self.signal_got_exit_request)
        widget.layout().addWidget(QLabel("Untappr: Hello World"))
        widget.layout().addWidget(btn)
        self.setCentralWidget(widget)

