from logic import *

# Background 
# A knight will always tell the truth, a knave will always lie.

# Objective
# Determine, for each character, whether that character is a knight or a knave.

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Biconditional(AKnight, Not(AKnave)),            # A is a Knight only if A is not a Knave
    Biconditional(AKnight, And(AKnight, AKnave))    # A is a Knight if "I am both a Knight and a Knave"
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Biconditional(AKnight, Not(AKnave)),            # A is a Knight only if A is not a Knave  
    Biconditional(BKnight, Not(BKnave)),            # B is a Knight only if B is not a Knave
    Biconditional(AKnight, And(AKnave, BKnave))     # A is a Knight only if "We are both Knaves"
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Biconditional(AKnight, Not(AKnave)),                                        # A is a Knight only if A is not a Knave  
    Biconditional(BKnight, Not(BKnave)),                                        # B is a Knight only if B is not a Knave
    Biconditional(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),     # A is a Knight if "We are the same kind"
    Biconditional(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave)))      # B is a Knight if "We are of different kinds"
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Biconditional(AKnight, Not(AKnave)),                                        # A is a Knight only if A is not a Knave  
    Biconditional(BKnight, Not(BKnave)),                                        # B is a Knight only if B is not a Knave
    Biconditional(CKnight, Not(CKnave)),                                        # C is a Knight only if C is not a Knave
    Or(Biconditional(AKnight, AKnight), Biconditional(AKnight, AKnave)),        # A is a Knight if "I am a Knight or Knave"
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),                     # B is a Knight if "A said I am a Knave"
    Biconditional(BKnight, CKnave),                                             # B is a Knight if "C is a Knave"
    Biconditional(CKnight, AKnight)                                             # C is a Knight if "A is a Knight"
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
