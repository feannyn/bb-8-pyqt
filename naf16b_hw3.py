import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QGridLayout, QBoxLayout, QHBoxLayout, QVBoxLayout, QSizePolicy, QWidget

class Homework3(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 450, 450)
        self.setWindowTitle("BB-8")
        self.DrawBB = DrawImage(self)
        self.initWidgets()
        self.setUpGrid()
        self.show()

    def initWidgets(self):

        self.left = self.makeButton("Left")
        self.right = self.makeButton("Right")
        self.top = self.makeButton("Top")
        self.bottom = self.makeButton("Bottom")
        self.addListeners()

    def setUpGrid(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.top, 0, 0, 1, 7) #all of these changes are inclusive
        self.grid.addWidget(self.left, 1, 0, 5, 1)
        self.grid.addWidget(self.right, 1, 6, 5, 1)
        self.grid.addWidget(self.bottom, 6, 0, 1, 7)
        self.grid.addWidget(self.DrawBB, 1, 1, 1, 1)

    def makeButton(self, side):
        button = QtWidgets.QPushButton(self)
        button.setText(side)
        if side == "Left" or side == "Right":
            button.setStyleSheet("background-color: #dfe6e9")
            button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        else:
            button.setStyleSheet("background-color: #fdcb6e")
        return button

    def leftButtonClicked(self):
        self.DrawBB.direction = "Left"
        self.DrawBB.update()

    def rightButtonClicked(self):
        self.DrawBB.direction = "Right"
        self.DrawBB.update()

    def topButtonClicked(self):
        self.DrawBB.direction = "Top"
        self.DrawBB.update()

    def bottomButtonClicked(self):
        self.DrawBB.direction = "Bottom"
        self.DrawBB.update()

    def addListeners(self):
        self.left.clicked.connect(self.leftButtonClicked)
        self.right.clicked.connect(self.rightButtonClicked)
        self.top.clicked.connect(self.topButtonClicked)
        self.bottom.clicked.connect(self.bottomButtonClicked)

class DrawImage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setFixedSize(350, 350)
        self.direction = "Top"

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(223, 230, 233))
        painter.drawEllipse(QPoint(200, 200), 100, 100)
        painter.setBrush(QColor(253, 203, 110))
        painter.drawEllipse(QPoint(200, 200), 60, 60)
        painter.setBrush(QColor(223, 230, 233))
        painter.drawEllipse(QPoint(200, 200), 25, 25)

        if self.direction == "Top":
            self.drawTop(painter)
        elif self.direction == "Left":
            self.drawLeft(painter)
        elif self.direction == "Right":
            self.drawRight(painter)
        elif self.direction == "Bottom":
            self.drawBottom(painter)

        painter.end()

    def drawTop(self, painter):
        painter.drawChord(137, 55, 130, 90, 0, (180 * 16))
        painter.setBrush(QColor(253, 203, 110))
        painter.drawChord(162, 77, 75, 45, 0, (180 * 16))
        painter.setBrush(QColor(223, 230, 233))

    def drawBottom(self, painter):
        painter.drawChord(135, 255, 130, 90, (180 * 16), (180 * 16))
        painter.setBrush(QColor(253, 203, 110))
        painter.drawChord(162, 278, 75, 45, (180 * 16), (180 * 16))
        painter.setBrush(QColor(223, 230, 233))

    def drawLeft(self, painter):
        painter.drawChord(55, 135, 90, 130, (90 * 16), (180 * 16))
        painter.setBrush(QColor(253, 203, 110))
        painter.drawChord(77, 165, 45, 75, (90 * 16), (180 * 16))
        painter.setBrush(QColor(223, 230, 233))

    def drawRight(self, painter):
        painter.drawChord(255, 135, 90, 130, (90 * 16), (-180 * 16))
        painter.setBrush(QColor(253, 203, 110))
        painter.drawChord(277, 165, 45, 75, (90 * 16), (-180 * 16))
        painter.setBrush(QColor(223, 230, 233))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    displayBB = Homework3()
    app.exec_()
