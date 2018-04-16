"""
cell module for minesweeper
"""

__author__ = "Joseph Hnatek"
__date__ = "April 4, 2018"

import turtle

class Cell(turtle.Turtle):
    def __init__(self, x=0, y=0):
        self.__bomb = False
        self.__x = x
        self.__y = y
        self.__adj = 0
        turtle.Turtle.__init__(self)
        
    @property
    def bomb(self):
        return self.__bomb

    @bomb.setter
    def bomb(self, val):
        self.__bomb = val

    @property
    def getX(self):
        return self.__x

    @property
    def getY(self):
        return self.__y

    @property
    def adj(self):
        return self.__adj

    @adj.setter
    def adj(self, num):
        self.__adj = num


    def reveal(self):
        if self.shape() != "question.gif":
            return False
        if self.bomb:
            self.shape("bomb.gif")
        else:
            self.shape(str(self.adj) + ".gif")
        return True
        
        

