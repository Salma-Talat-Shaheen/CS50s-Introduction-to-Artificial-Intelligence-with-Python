# Tic-Tac-Toe AI with Minimax Algorithm

## Project Overview

The goal of this project is to implement an AI that plays Tic-Tac-Toe optimally using the **Minimax Algorithm**. The project consists of implementing various functions to simulate and play the game. These functions will handle tasks such as determining the current player's turn, checking for possible actions, evaluating the game state, and determining the best move for the AI.

### Python Version
- **Recommended Python version**: Python 3.12

---

## Getting Started

### Setup

1. **Download the distribution**:
   - Download the code from [this link](https://cdn.cs50.net/ai/2023/x/projects/0/tictactoe.zip) and unzip it.

2. **Install the required dependencies**:
   - Navigate to the directory of the project and run the following command to install the required Python package (`pygame`):
     ```bash
     pip3 install -r requirements.txt
     ```

### Files in the Project

- **`runner.py`**: Contains the code for the graphical interface of the game. You do not need to modify this file.
- **`tictactoe.py`**: Contains the logic for the game, including AI behavior. This is where you will implement the required functions.

### Game Representation

The game is represented as a 3x3 grid, where each cell can either be `X`, `O`, or `EMPTY`. The functions in the project will operate on this grid to determine the game's state and the optimal move for the AI.

---

## Specifications

### Functions to Implement

1. **`player(board)`**:
   - **Input**: `board` (a list of lists representing the game state).
   - **Output**: The player whose turn it is ('X' or 'O').
   - **Description**: The function returns the player whose turn it is based on the current board state. `X` starts first. 

2. **`actions(board)`**:
   - **Input**: `board` (a list of lists representing the game state).
   - **Output**: A set of all possible actions (as tuples `(i, j)`) where `i` is the row and `j` is the column.
   - **Description**: The function returns all available moves where a cell is still `EMPTY`.

3. **`result(board, action)`**:
   - **Input**: `board` (current game state), `action` (a tuple `(i, j)` representing a move).
   - **Output**: A new board state with the move applied.
   - **Description**: Given a board and a valid action, the function returns a new board with the move applied. The original board should remain unmodified.

4. **`winner(board)`**:
   - **Input**: `board` (current game state).
   - **Output**: `X`, `O`, or `None`.
   - **Description**: The function checks if there is a winner. Returns `X` if X has won, `O` if O has won, or `None` if there is no winner yet.

5. **`terminal(board)`**:
   - **Input**: `board` (current game state).
   - **Output**: `True` or `False`.
   - **Description**: This function checks if the game is over (either a player has won or the board is full and it’s a tie).

6. **`utility(board)`**:
   - **Input**: `board` (a terminal board).
   - **Output**: `1`, `-1`, or `0`.
   - **Description**: The utility function returns `1` if `X` has won, `-1` if `O` has won, or `0` if the game ended in a tie.

7. **`minimax(board)`**:
   - **Input**: `board` (current game state).
   - **Output**: A tuple `(i, j)` representing the optimal move for the current player.
   - **Description**: The minimax function should calculate the optimal move for the current player using the minimax algorithm.

### Game Flow

- **Start the game**: The game starts with the function `initial_state`, which initializes the board with all cells set to `EMPTY`.
- **Gameplay**: 
   - The game alternates between players (`X` and `O`).
   - The current player will make the optimal move using the `minimax` function.
   - The game will continue until there is a winner or the game ends in a tie.

### How to Play

Once you have implemented the functions, you can run the game using the `runner.py` script:

```bash
python runner.py
