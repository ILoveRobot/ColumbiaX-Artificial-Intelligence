"""
AI agent that solves the n-sliding puzzle game through various search algorithms

Starting the script
-------------------
python driver.py <method> <board>

Parameters
----------
The method argument will be one of the following.
bfs (Breadth-First Search)
dfs (Depth-First Search)
ast (A-Star Search)
ida (IDA-Star Search)

The board argument will be a comma-separated list of integers containing no spaces that represents
that initial state of the puzzle board


Example Script Execution
-----------------
python driver.py bfs 0,8,7,6,5,4,3,2,1

Output
------
When executed, the program will write to a file called output.txt, containing the following statistics:

path_to_goal: the sequence of moves taken to reach the goal
cost_of_path: the number of moves taken to reach the goal
nodes_expanded: the number of nodes that have been expanded
fringe_size: the size of the frontier set when the goal node is found
max_fringe_size: the maximum size of the frontier set in the lifetime of the algorithm
search_depth: the depth within the search tree when the goal node is found
max_search_depth:  the maximum depth of the search tree in the lifetime of the algorithm
running_time: the total running time of the search instance, reported in seconds
max_ram_usage: the maximum RAM usage in the lifetime of the process reported in megabytes

"""

import sys
import boardState
import Board

method = sys.argv[1]
board = sys.argv[2]

startState = boardState.BoardState(None, board, [])
puzzleBoard = Board.Board(startState)

print(puzzleBoard.board)


if method == "bfs":
    print("")
elif method == "dfs":
    print("")
elif method == "ast":
    print("")
elif method == "ida":
    print("")
