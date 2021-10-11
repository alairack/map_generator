from PyQt5.QtWidgets import (QWidget, QLabel, QScrollArea, QMessageBox,
                             QVBoxLayout, QMainWindow, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Widget)
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)               # 设置边距为0,防止控件四周出现空白
        self.gridlayout = QGridLayout()
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(0)
        self.load_image()
        self.vbox.addLayout(self.gridlayout)
        self.widget.setLayout(self.vbox)
        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu.setTitle("文件")
        self.setMenuBar(self.menuBar)
        self.save_image = QtWidgets.QAction(self)
        self.save_image.setObjectName("save_image")
        self.save_image.setText("保存为图片")
        self.save_image.setToolTip("把当前生成的地图保存为图片")
        self.save_image.setEnabled(True)
        self.save_image.setShortcut("Ctrl+S")
        self.save_image.triggered.connect(self.save)
        self.menu.addAction(self.save_image)
        self.menuBar.addAction(self.menu.menuAction())
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
        try:
            with open('export.txt', "r") as f:
                content = f.read()
                content = content.replace(" ", "")
                config = read_config()
                x = 0
                y = 0
                for ch in content:
                    if ch != "\n":
                        ch = config[int(ch)]
                        self.add_texture("./texture/" + ch + ".png", y, x)
                        x = x + 1
                    else:
                        y = y + 1
                        x = 0
        except FileNotFoundError:
            QMessageBox.critical(None, '错误', '读取输入文件(export.txt)失败！')
            sys.exit(3)

    def save(self):
        self.widget.grab().save('map_save.png')
        QMessageBox.information(self, "状态", "已成功保存至当前目录！")


def read_config():
    try:
        with open("config.txt", 'r') as f:
            config_content = f.read()
            config_content = config_content.replace(" ", "")
            config_content = config_content.splitlines()
            config = []
            for line in config_content:
                config.insert(int(line[0]), line[1:])
        return config
    except FileNotFoundError:
        QMessageBox.critical(None, '警告', "未能成功读取配置文件(config.txt)!")
        sys.exit(4)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
