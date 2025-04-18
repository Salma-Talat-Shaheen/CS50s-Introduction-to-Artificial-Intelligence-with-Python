from tictactoe import initial_state
from tictactoe import player
from tictactoe import actions
from tictactoe import result
from tictactoe import winner
from tictactoe import terminal
from tictactoe import utility
from tictactoe import minimax

board = initial_state()
actions = actions(board)
winner = winner(board)
terminal = terminal(board)
utility = utility(board)
minimax = minimax(board)
print(minimax)
