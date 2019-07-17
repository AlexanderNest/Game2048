import random
from numpy import array, flip
import os


class Board:
    def __init__(self, size, start_score, default=None):
        self.size = size
        self.score = 0
        if default is None:
            self.board = array([[-1 for x in range(self.size)] for i in range(self.size)])  # if not a number then -1
        else:
            self.board = array([
                [4, 2, 2],
                [4, -1, -1],
                [-1, 4, -1]
            ])
        self.start_score = start_score
        self.generate_start(start_score)  # define start position
        self.last = self.board.copy()
        self.last_score = 0

        # TODO добавить проверку окончания игры

    def isfull(self):
        for i in self.board:
            for k in i:
                if k == -1:
                    return False
        return True

    def restart(self):
        self.board = array([[-1 for x in range(self.size)] for i in range(self.size)])
        self.generate_start(self.start_score)
        self.score = 0

    def undoboard(self):
        self.board = self.last
        self.score = self.last_score

    def leftshift(self, func=None):
        self.last_score = self.score
        self.last = self.board.copy()
        shifted = False
        while True:
            hasshiftes = False
            for y in range(self.size):
                for x in range(self.size):

                    if x > 0 and self.board[y][x] != -1:
                        if self.board[y][x - 1] == -1:
                            self.board[y][x - 1] = self.board[y][x]
                            self.board[y][x] = -1
                            hasshiftes = True
                            shifted = True
                        else:
                            if self.board[y][x] == self.board[y][x - 1]:
                                self.board[y][x - 1] *= 2
                                self.score += self.board[y][x - 1]
                                self.board[y][x] = -1
                                hasshiftes = True
                                shifted = True

            if not hasshiftes:
                break

        if shifted:
            self.generate_cell()

    def rightshift(self, func=None):
        self.last_score = self.score
        self.last = self.board.copy()
        shifted = False
        while True:
            hasshiftes = False
            for y in range(self.size):
                for x in range(self.size):

                    if x < self.size - 1 and self.board[y][x] != -1:
                        if self.board[y][x + 1] == -1:
                            self.board[y][x + 1] = self.board[y][x]
                            self.board[y][x] = -1
                            hasshiftes = True
                            shifted = True
                        else:
                            if self.board[y][x] == self.board[y][x + 1]:
                                self.board[y][x + 1] *= 2
                                self.score += self.board[y][x + 1]
                                self.board[y][x] = -1
                                hasshiftes = True
                                shifted = True

            if not hasshiftes:
                break
        if shifted:
            self.generate_cell()

    def upshift(self):
        self.board = self.board.T
        self.leftshift('func')
        self.board = self.board.T

    def bottomshift(self):
        self.board = self.board.T
        self.rightshift('func')
        self.board = self.board.T

    def getstate(self):
        print('Очки = ', self.score)
        print()
        for i in range(7 * self.size):
            print('-', end='')
        print()
        for i in self.board:
            for k in i:
                if k == -1:
                    print('|', '%+3s' % ' ', '|', end='')
                else:
                    print('|', '%+3s' % k, '|', end='')
            print()
            for i in range(7 * self.size):
                print('-', end='')
            print()

    def generate_start(self, start_score):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)

        self.board[x][y] = start_score

    def generate_cell(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.board[x][y] == -1:
                self.board[x][y] = 2
                break
            if self.isfull():
                break
