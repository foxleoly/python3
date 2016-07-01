#! python
# -*- coding: utf-8 -*-
"""
The script to make a widget and display a tooltips when the mouse move to button and windows

"""
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton,QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):


    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont("SanSerif", 10))

        self.setToolTip("This is a <b>Qwidget</b> widget!")

        btn = QPushButton("Button", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget!")
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,180)
        self.setWindowTitle("ToolTips")
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
