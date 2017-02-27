"""
This class represents the physical configuration of the a n-sliding puzzle
and possible actions you can do with a real world n-sliding puzzle
"""

class Board:

    def __init__(self, state):
        self.board = self.buildBoard(state)

    """
    Creates the a n-sliding puzzle board given a state of the board

    Parameters
    ----------
    state: BoardState
        reference to the state of a board this object will represent

    Returns
    -------
    2D integer array
        represents the NxN board
    """
    def buildBoard(self, state):
        bd = state.board.split(',')
        bd = [int(i) for i in bd]        

        i = 0
        nCnt = int(len(bd)**.5)
        board = []

        for x in range(nCnt):
            row = []

            for y in range(nCnt):
                row.append(bd[i])
                i += 1

            board.append(row)

        return board

    """
    Creates a new board state that is the result of moving the
    empty space(0) in the n-sliding puzzle

    Parameters
    ----------
    dir: String
        the direction to move the empty space in the puzzle

    Returns
    --------
    String
        the string representation of state of the board that results from moving the empty space
    """
    #def move(self, dir):


    """
    Swaps 2 tiles in the board

    Parameters
    ----------
    t1: tuple
        the coordinates of the 1st tile in board
    t2: tuple
        the coordinates of the 2nd tile in board

    Returns
    -------
    String
       the string representation of state of the board that results from moving the empty space        
    """
    #def swapTiles(a, b):

    """
    Finds the coordinates of the empty space(0) in the board

    Returns
    -------
    tuple
        the coordinates of the empty tile in board
    """
    #def findEmptyTile():
