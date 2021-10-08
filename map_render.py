import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'map_render'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.gridlayout = QGridLayout()
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(0)
        self.setLayout(self.gridlayout)
        self.show()
        self.setFixedSize(self.gridlayout.sizeHint())

    def add_texture(self, image_path, layout_row, layout_column):
        pixmap = QPixmap(image_path)
        pixmap_2 = pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        label = QLabel(self)
        label.setPixmap(pixmap_2)
        self.gridlayout.addWidget(label, layout_row, layout_column, 1, 1)


def main(window):
    with open('export.txt', "r") as f:
            content = f.read()
            content = content.replace(" ", "")
            convert = ["grass", "soil", "blue_brick", "magma", "bird", "fish", "tree", "friend", "boss", "diamond"]
            x = 0
            y = 0
            for ch in content:
                if ch != "\n":
                    ch = convert[int(ch)]
                    window.add_texture("./texture/" + ch + ".png", y, x)
                    x = x + 1
                else:
                    y = y+1
                    x = 0

    return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    render_window = MainWindow()
    main(render_window)
    sys.exit(app.exec_())