# Knights

## Overview

Write a program to solve logic puzzles using propositional logic and model checking.

### Deadline
**By Thursday, January 1, 2026 at 1:59 AM GMT+2**

---

## Background

In 1978, logician Raymond Smullyan published *What is the Name of This Book?*, a collection of logical puzzles. Among them were “Knights and Knaves” puzzles.

- **Knights** always tell the truth.
- **Knaves** always lie.

Each character in a puzzle is either a knight or a knave. Given the statements each character makes, your goal is to determine whether each character is a knight or a knave using propositional logic.

---

## Example

Consider a simple puzzle:

> A says: “I am both a knight and a knave.”

If A were a knight, the statement would be true—but a character cannot be both a knight and a knave. Therefore, A must be lying, which means A is a knave.

---

## Objective

Your task is to represent each puzzle using propositional logic so that a model-checking AI can solve it automatically.

---

## Getting Started

1. Download the starter files:  
   [knights.zip](https://cdn.cs50.net/ai/2023/x/projects/1/knights.zip)
2. Unzip the archive and explore the files.

---

## Provided Files

- `logic.py`: Contains classes for propositional logic expressions (`Symbol`, `And`, `Or`, `Not`, `Implication`) and the `model_check` function.
- `puzzle.py`: Where you will write the logic for each puzzle.

---

## Symbols Defined

In `puzzle.py`, six propositional symbols are already defined:

- `AKnight`, `AKnave`: A is a knight or knave.
- `BKnight`, `BKnave`: B is a knight or knave.
- `CKnight`, `CKnave`: C is a knight or knave.

---

## The Puzzles

Fill in the knowledge bases `knowledge0` through `knowledge3` to solve the following puzzles:

### Puzzle 0
- Characters: A
- Statement: A says “I am both a knight and a knave.”

### Puzzle 1
- Characters: A, B
- Statements:
  - A says “We are both knaves.”
  - B says nothing.

### Puzzle 2
- Characters: A, B
- Statements:
  - A says “We are the same kind.”
  - B says “We are of different kinds.”

### Puzzle 3
- Characters: A, B, C
- Statements:
  - A says either “I am a knight.” or “I am a knave.” (you don’t know which).
  - B says “A said ‘I am a knave.’”
  - B also says “C is a knave.”
  - C says “A is a knight.”

---

## Specification

- For each puzzle, define a **knowledge base** containing:
  1. Rules of the world (e.g., each person is either a knight or a knave, but not both)
  2. Logical representation of each statement made
- Use the `model_check` function to determine the status of each character.

To run the program and see results:
```bash
python puzzle.py
```

---

## Tips

- For each knowledge base, encode:
  - The structure of the world (knight/knave rules)
  - The meaning of the statements made
- Use logical expressions such as `Implication`, `And`, `Or`, `Not`
- Avoid hardcoding solutions like `knowledge0 = AKnave`. Let the model checker derive this logically.

---

## Note

- You **do not** need to modify `logic.py`.
- Multiple valid knowledge bases can produce the correct result—aim for clarity and conciseness.
