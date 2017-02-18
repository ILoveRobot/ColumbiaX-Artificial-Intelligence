"""
Helper class that checks if a given boardState has been solved. Also keeps
track of previously visited boardStates
"""

class Solver:

    def __init__(self):
        self.visited = {}

    """
    Checks whether a given boardState is the goal boardState

    Parameters
    ----------
    state: boardState
        reference to the boardState to check

    Returns
    -------
    boolean
        True if state is the goal state, False otherwise
    """
    def isSolved(self, state):
        board = state.board.split(',')
        board = [int(i) for i in board]

        goal = [int(i) for i in range(0,len(board))]

        if(board == goal):
            return True

        return False
