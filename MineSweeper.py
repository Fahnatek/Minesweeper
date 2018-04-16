"""
Minesweeper
"""

__author__ = "Joseph Hnatek"
__date__ = "March 12, 2018"

import game
import turtle


def main():
    def tick(x, y):
        cellsProbed, bombLeft = gameBoard.probe(x, y)
        if (bombLeft == numBombs and cellsProbed == ((boardSize **2) - numBombs)) or bombLeft < numBombs:
            c = turtle.textinput("Number of tries: {}".format(cellsProbed),\
                              "Play again? (y)es or (n)o?: ")
            if c == "y":
                main()
            elif c == "n":
                turtle.bye()

    boardSize = int(turtle.numinput("Minesweeper", "Board Size? (size x size)"))
    totCells = boardSize * boardSize
    gameBoard = game.Game(boardSize)

    done = False
    while not done:
        numBombs = int(turtle.numinput("Minesweeper",\
                                   "How many bombs do you want to hide?"))
        done = gameBoard.hideMines(numBombs)

    turtle.onscreenclick(tick)
    turtle.mainloop()#  Pycharm closes automatically, need this to keep it open.

    
main()
