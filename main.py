#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

One line, under 200 characters, in which a dog explains why the
homework got eaten. The program scores ten fresh candidate excuses
against the judge's brief (in order: dog's excuse in the dog's own
voice; bigger laugh with a twist or dog logic; sounds like a real
dog; works on its own; fresh) and writes the winner to
/output/entry.txt.
"""

CANDIDATES = [
    # 1
    "You told me to sit, stay, and do my homework. I sat. I stayed. "
    "I did the homework. It took one bite.",
    # 2
    "I ate it because the essay was about the life cycle of a chicken, "
    "and I believe in finishing what nature started.",
    # 3
    "The homework smelled like your hands, and your hands smell like "
    "bacon, so technically the homework started it.",
    # 4
    "I didn't eat your homework. The homework entered my mouth during "
    "a routine floor inspection. I am a professional.",
    # 5
    "It was the only homework in the house that smelled like chicken "
    "nuggets. I followed the evidence. I'm basically a detective.",
    # 6
    "The homework was on the floor, and the floor is where food lives. "
    "I was just tidying up. You should thank me.",
    # 7
    "You said to eat, sleep and breathe homework. I started with "
    "eating. I'm the only one in class who did it literally.",
    # 8
    "I saved you from it. That essay was going to ruin your weekend, "
    "so I took one for the team. You're welcome.",
    # 9
    "The homework asked to be eaten. It lay there smelling of your "
    "hands, whispering bacon. I am a dog, not a saint.",
    # 10
    "It looked at me. It was paper. Paper is food that hasn't admitted "
    "it yet, and I am very good at spotting food.",
]

# Judge criteria in order, weights 5/4/3/2/1:
#   1. dog's excuse in the dog's own voice (caught eating homework)
#   2. bigger laugh, twist / dog logic landing in the line
#   3. sounds like a real dog, dog priorities, no human embarrassment
#   4. works on its own, no setup, nothing needing a second line
#   5. fresh, not a stock line about the cat, the taste of paper,
#      or being a good boy
CRITERIA = [
    ("dog_voice", 5),
    ("laugh_twist", 4),
    ("real_dog", 3),
    ("standalone", 2),
    ("fresh", 1),
]

# Scores per candidate, per criterion (0-5). Judged by hand against
# the brief: the dog must believe it did nothing wrong, the twist
# must land in the last few words, and the line must be a dog's
# logic, not a person's apology.
SCORES = {
    1: {"dog_voice": 5, "laugh_twist": 5, "real_dog": 5,
        "standalone": 5, "fresh": 5},
    2: {"dog_voice": 5, "laugh_twist": 5, "real_dog": 5,
        "standalone": 5, "fresh": 4},
    3: {"dog_voice": 5, "laugh_twist": 4, "real_dog": 5,
        "standalone": 5, "fresh": 4},
    4: {"dog_voice": 5, "laugh_twist": 4, "real_dog": 4,
        "standalone": 5, "fresh": 4},
    5: {"dog_voice": 5, "laugh_twist": 4, "real_dog": 5,
        "standalone": 5, "fresh": 3},
    6: {"dog_voice": 5, "laugh_twist": 3, "real_dog": 5,
        "standalone": 5, "fresh": 3},
    7: {"dog_voice": 5, "laugh_twist": 4, "real_dog": 4,
        "standalone": 4, "fresh": 4},
    8: {"dog_voice": 4, "laugh_twist": 3, "real_dog": 4,
        "standalone": 5, "fresh": 3},
    9: {"dog_voice": 5, "laugh_twist": 4, "real_dog": 4,
        "standalone": 5, "fresh": 3},
    10: {"dog_voice": 5, "laugh_twist": 3, "real_dog": 5,
         "standalone": 5, "fresh": 2},
}


def score(candidate_no):
    """Weighted total for one candidate, plus its length."""
    total = sum(SCORES[candidate_no][name] * weight
                for name, weight in CRITERIA)
    return total, len(CANDIDATES[candidate_no - 1])


def rank():
    """Candidates ranked best first; ties broken by shorter line."""
    ranked = sorted(
        range(1, len(CANDIDATES) + 1),
        key=lambda n: (-score(n)[0], score(n)[1]),
    )
    return [(n, score(n)[0], score(n)[1]) for n in ranked]


def show_ranking():
    for n, total, length in rank():
        print(f"#{n:>2} score={total:>2}/75 chars={length:>3} "
              f"{CANDIDATES[n - 1]}")


def pick_winner():
    """Highest score wins; ties broken by the shorter line."""
    ranked = rank()
    winner_no, total, length = ranked[0]
    return CANDIDATES[winner_no - 1], winner_no, total, length


def validate(text):
    """The gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    show_ranking()
    winner, winner_no, total, length = pick_winner()
    validate(winner)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"\nwinner: #{winner_no} score={total}/75 chars={length}")
    print(winner)


if __name__ == "__main__":
    main()
