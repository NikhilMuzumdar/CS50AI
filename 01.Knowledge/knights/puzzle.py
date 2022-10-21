from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

general_knowledge = And(
                Or(AKnight,AKnave), # Can't be both
                Or(BKnight,BKnave), # Can't be both
                Or(BKnight,BKnave), # Can't be bothn
                )
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
                general_knowledge,
                # If A is a Knight, "I am both a knight and a knave." is True
                Implication(AKnight, And(AKnight, AKnave)),
                # If A is a Knave, "I am both a knight and a knave." is not True
                Implication(AKnave, Not(And(AKnight, AKnave))),
                )


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
                general_knowledge,
                # If A is a Knight, "We are both knaves." is True
                Implication(AKnight, And(BKnave, AKnave)),
                # If A is a Knave, "We are both knaves." is not True
                Implication(AKnave, Not(And(BKnave, AKnave))),
                )

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
                general_knowledge,
                # A says "We are the same kind." Implies:
                # A is a Knight - A and B are Knights is true
                Implication(AKnight, And(AKnight, BKnight)),
                # A is a Knight - A and B are Knaves is true
                Implication(AKnight, And(AKnave, BKnave)),
                # A is a Knave - A and B are Knights is not true
                Implication(AKnave, Not(And(AKnight, BKnight))),
                # A is a Knave - A and B are Knaves is not true
                Implication(AKnave, Not(And(AKnave, BKnave))),

                # B says "We are of different kinds." Implies:
                # B is a Knight - Either of A and B are Knights is true
                Implication(BKnight, Or(AKnight, BKnight)),
                # B is a Knight - Either of A and B are Knaves is true
                Implication(BKnight, Or(AKnave, BKnave)),
                # B is a Knave - Either of A and B are Knights is not true
                Implication(BKnave, Not(Or(AKnight, BKnight))),
                # B is a Knave - Either of A and B are Knaves is not true
                Implication(BKnave, Not(Or(AKnave, BKnave))),
                )

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
                general_knowledge,
                # A says either "I am a knight." or "I am a knave.", but you don't know which.
                Implication(AKnight, Or(AKnight, AKnave)),
                Implication(AKnave, Not(Or(AKnight, AKnave))),

                # B says "A said 'I am a knave'."
                # Assuming B is a Knight, A could be Kinght or a Knave
                Implication(BKnight, Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),
                # Assuming B is a Knave, A could be Knight or a Knace
                Implication(BKnave, Or(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight)))),


                # B says "C is a knave."
                # Implies if B is a Knight, C is a Knave or B is a Knave and C is a Knight
                Implication(BKnight, CKnave),
                Implication(BKnave, CKnight),

                # C says "A is a knight."
                # Implies if C is a Knight, A is a Knight or if C is a Knave, A is a Knace
                Implication(CKnight, AKnight),
                Implication(CKnave, AKnave),

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
