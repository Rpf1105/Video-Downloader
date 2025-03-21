import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Downloader")
        self.setGeometry(0, 0, 800, 400)
        self.setWindowIcon(QIcon("icon.png"))
        self.setStyleSheet(
            "background-color: #DDDDDD"
        )
        self.initUi()

    def initUi(self):
        center_widget = QWidget()
        self.setCentralWidget(center_widget)
        label1 = DefaultLabel("link do video", self)
        label2 = DefaultLabel("enviar", self)

        grid = QVBoxLayout()

        grid.addWidget(label1)
        grid.addWidget(label2)

        center_widget.setLayout(grid)



class DefaultLabel(QLabel):
    def __init__(self, text: str, parent=None):
        QLabel.__init__(self, parent)
        self.setFont(QFont("Arial", 12))
        self.setStyleSheet(
            "color: #333333;"
        )
        self.setAlignment(Qt.AlignCenter)
        self.setText(text)

def main():
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    sys.exit(app.exec_())

main()