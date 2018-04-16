"""
game handler for minesweeper
"""

__author__ = "Joseph Hnatek"
__date__ = "March 16, 2018"

import turtle
import cell
import random


class Game:
    def __init__(self, size):

        self.__boardSize = size
        self.__board = []
        self.__numofBomb = 0
        self.__cellsProbed = 0

        registerShapes()
        scale = (self.__boardSize) * 15

        for row in range(self.__boardSize):  
            for col in range(self.__boardSize):

                t = cell.Cell(row, col)
                t.penup()
                t.shape("question.gif")
                t.goto(((col * 34) - scale), ((scale - (row * 34))))
                self.__board.append(t)


    def hideMines(self, num):
        if num < len(self.__board):
            self.__numofBomb = num

            while num > 0:
                cellT = random.choice(self.__board)
                               
                if not cellT.bomb:
                    cellT.bomb = True
                    num = num - 1

            return True
        return False


    def probe(self, x, y):
        closest = self.__board[0]
        dist = closest.distance(x, y)

        for z in self.__board:
            d = z.distance(x, y)
            if d < dist:
                closest = z
                dist = d

        closest.adj = self.checkAdj(closest)

        if closest.reveal():
            self.__cellsProbed = self.__cellsProbed + 1
            if closest.bomb:
                self.__numofBomb = self.__numofBomb - 1

        return self.__cellsProbed, self.__numofBomb


    def checkAdj(self, obj):
        x = obj.getX
        y = obj.getY

        minX = max(0, x - 1)
        minY = max(0, y - 1)
        maxX = min(self.__boardSize, x + 2)
        maxY = min(self.__boardSize, y + 2)

        numBomb = 0

        for row in range(minX, maxX):
            for col in range(minY, maxY):

                val = (row * self.__boardSize) + col
                if self.__board[val].bomb:
                    numBomb = numBomb + 1

        return numBomb


def registerShapes():
    for x in range(10):
        turtle.register_shape(str(x) + ".gif")
    turtle.register_shape('bomb.gif')
    turtle.register_shape('question.gif')



