from PyQt5.QtWidgets import (QWidget, QLabel, QScrollArea, QApplication,
                             QVBoxLayout, QMainWindow, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        self.gridlayout = QGridLayout()
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(0)
        self.load_image()
        self.vbox.addLayout(self.gridlayout)
        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.setWindowTitle('map_render')
        self.show()

    def add_texture(self, image_path, layout_row, layout_column):
        pixmap = QPixmap(image_path)
        pixmap_2 = pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        label = QLabel()
        label.setPixmap(pixmap_2)
        label.setScaledContents(True)
        self.gridlayout.addWidget(label, layout_row, layout_column, 1, 1)

    def load_image(self):
        with open('export.txt', "r") as f:
            content = f.read()
            content = content.replace(" ", "")
            convert = ["grass", "soil", "blue_brick", "magma", "bird", "fish", "tree", "friend", "boss", "diamond"]
            x = 0
            y = 0
            for ch in content:
                if ch != "\n":
                    ch = convert[int(ch)]
                    self.add_texture("./texture/" + ch + ".png", y, x)
                    x = x + 1
                else:
                    y = y + 1
                    x = 0
        return 0


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
