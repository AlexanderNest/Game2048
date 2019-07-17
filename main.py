import board as board
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp

import Board
import msvcrt
import time
import os
from UI import *


class Game(QMainWindow):
    def __init__(self):
        super().__init__()

        self.game = UI2048()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    userInterface = Game()
    sys.exit(app.exec_())
