# Minesweeper AI Project

## Deadline
**Due:** Thursday, January 1, 2026 at 1:59 AM (GMT+2)  
**Python Version:** Use Python 3.12

## Objective
Design and implement an AI that can play the game **Minesweeper** using propositional logic and inference.

---

## Game Overview

**Minesweeper** is a puzzle game consisting of a grid of cells. Some cells contain hidden mines, while others are safe.

- Clicking on a mine results in losing the game.
- Clicking on a safe cell reveals a number indicating how many neighboring cells contain mines.
- The goal is to flag all mines using logical inference based on the numbers shown.

---

## Key Concepts

### Propositional Logic
- Each cell is a propositional variable: `True` if it contains a mine, `False` otherwise.
- Revealing a safe cell provides a number `n`, meaning exactly `n` neighboring cells are mines.
- This leads to logical expressions like:  
  `{A, B, C, D, E, F, G, H} = 1`  
  This means exactly 1 of the listed cells is a mine.

### Knowledge Representation
- Each **Sentence** has:
  - A **set of cells**
  - A **mine count**

#### Inference Rules
- If count = 0 → all cells are safe.
- If count = number of cells → all cells are mines.
- Sentences can be updated when new information is known.
- Subset inference:  
  If `S1 = c1` and `S1 ⊂ S2` with `S2 = c2`, then  
  `S2 - S1 = c2 - c1`

---

## Files and Setup

1. Download and unzip the starter code:
   [minesweeper.zip](https://cdn.cs50.net/ai/2023/x/projects/1/minesweeper.zip)
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
