"""
Represents any given state of the board for the
n-sliding puzzle game

"""

class BoardState:
    """
    Constructor that sets up the member variables for instantiated boardState

    Parameters
    ----------
    parent: boardState
        reference to the parent boardState
        
    board: string
        string representation of the sliding puzzle board for this state
        
    moves: string[]
        the sequence of moves that it took to reach this board state
    """
    def __init__(self, parent, board, moves):
        self.parent = parent
        self.board = board
        self.moves = moves
        self.children = {"up": None, "down": None, "left": None, "right": None}
