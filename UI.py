import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont
from Board import Board


class UI2048(QWidget):

    def __init__(self):
        super().__init__()
        self.board = Board(2, 2)
        self.board.getstate()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Decorative', 24))
        print(self.size().height())
        qp.drawText(5, self.size().height() - 5, "Очки = " + str(self.board.score))
        qp.end()

    def keyPressEvent(self, QKeyEvent):

        if QKeyEvent.key() == QtCore.Qt.Key_Left:
            self.board.leftshift()
            self.moving = True
            self.update()
        elif QKeyEvent.key() == QtCore.Qt.Key_Right:
            self.board.rightshift()
            self.update()
        elif QKeyEvent.key() == QtCore.Qt.Key_Up:
            self.board.upshift()
            self.update()
        elif QKeyEvent.key() == QtCore.Qt.Key_Down:
            self.board.bottomshift()
            self.update()
        elif QKeyEvent.key() == QtCore.Qt.Key_Z:
            self.board.undoboard()
            self.update()
        elif QKeyEvent.key() == QtCore.Qt.Key_R:
            self.board.restart()
            self.update()

        self.board.getstate()

    def drawRectangles(self, qp, direction=None):
        col = QColor(0, 0, 0)

        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        background_size = self.board.size * 120 + (self.board.size + 1) * 10

        self.setFixedSize(background_size, background_size + 30)
        qp.setBrush(QColor(102, 102, 102))
        qp.drawRect(0, 0, background_size, background_size)
        y = 10

        for i in range(self.board.size):
            x = 10
            for k in range(self.board.size):
                qp.setBrush(QColor(204, 204, 204))
                qp.drawRect(x, y, 120, 120)
                if self.board.board[i][k] != -1:
                    qp.setBrush(QColor(255, 140, 0))
                    qp.drawRect(x, y, 120, 120)
                    qp.setPen(QColor(255, 255, 255))
                    qp.setFont(QFont('Decorative', 30))
                    qp.drawText(x + 50, y + 75, str(self.board.board[i][k]))
                x += 130
            y += 130
