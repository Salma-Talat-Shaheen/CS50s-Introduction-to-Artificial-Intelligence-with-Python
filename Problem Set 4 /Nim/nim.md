# Nim Reinforcement Learning AI

This project implements an AI that learns to play the game of **Nim** using **Q-learning**, a type of reinforcement learning. The AI starts off with no strategy and gradually improves by playing against itself, learning from each move it makes.

## Overview

**Nim** is a game in which players take turns removing objects from piles. The player who removes the last object loses. The AI in this project learns the optimal strategy to minimize its chances of losing.

The AI uses **Q-learning** to learn this strategy. In Q-learning, the AI learns by associating each state (the configuration of piles) with a value called a Q-value. The AI updates its Q-values based on its actions, where it tries to maximize the long-term reward. A reward is given after each move:
- **-1** if the action results in a loss.
- **1** if the action results in the opponent losing.
- **0** if the game continues.

### Game Mechanics
- The game is played between two players who take turns.
- On each turn, a player removes objects from a pile. The number of objects to remove and the pile from which to remove them are chosen as an **action**.
- The AI learns which actions lead to winning and which ones lead to losing.

## Components

### Files in the Project
- **`nim.py`**: Contains the main game logic, including the Nim class (which defines the game and its mechanics) and the NimAI class (which defines the AI and its Q-learning-based decision-making).
- **`train.py`**: A script that trains the AI by running several games against itself. The AI updates its Q-values as it plays.
- **`play.py`**: A script that allows a human player to play against the trained AI.

### Key Functions in `nim.py`
1. **Nim Class**: Defines the game setup, including the piles, available actions, and game rules. It also handles player turns and the game state.
2. **NimAI Class**: Defines the AI, including its Q-learning methods. The AI stores Q-values in a dictionary and uses them to decide which actions to take.
3. **Q-learning**:
   - The AI updates Q-values using the formula:
     \[
     Q(s, a) \leftarrow Q(s, a) + \alpha \times (\text{{reward}} + \gamma \times \text{{best future reward}} - Q(s, a))
     \]
   - **`alpha`** is the learning rate, **`gamma`** is the discount factor, and the **`epsilon`** value controls exploration vs exploitation.
   
### How to Play and Train the AI

1. **Training**:
   - The AI plays 10,000 games against itself to learn the best strategies. During these games, it explores different actions, evaluates their outcomes, and updates its Q-values.
   - To start the training process, run:
     ```bash
     python train.py
     ```
   - The AI will play games, updating its Q-values, and will be ready for interaction once training is complete.

2. **Playing**:
   - After training, you can play against the AI using:
     ```bash
     python play.py
     ```
   - The human player takes turns with the AI. The AI chooses its moves based on the learned Q-values.

### Customizing the Training Process
You can adjust the following parameters to experiment with the training:
- **`alpha` (Learning Rate)**: Controls how much the AI values new experiences versus existing knowledge.
- **`gamma` (Discount Factor)**: Determines the importance of future rewards in the decision-making process.
- **`epsilon` (Exploration Rate)**: Controls the likelihood of the AI exploring random actions rather than exploiting known good actions. A high epsilon means more exploration, while a low epsilon means more exploitation.

For example, in `train.py`:
```python
alpha = 0.1    # Learning rate
gamma = 0.9    # Discount factor
epsilon = 0.2  # Exploration rate

