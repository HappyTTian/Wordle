import pathlib
import random

words = [
    word.lower()
    for word in pathlib.Path("wordList.txt").read_text(encoding="utf-8").strip().split('\n')
]
answer = random.choice(words)
for i in range(6):
    guess = input(f"Guess {i+1}: ").lower()
    if guess == answer:
        print ("Correct")
        break

    correct_letters = {c1 for c1,c2 in zip(answer,guess) if c1 == c2}
    misplace_letters = set(answer) & set(guess) - correct_letters
    wrong_letters = set(guess) - set(answer)
    print ("Correct letters: ", ", ".join(correct_letters))
    print ("Misplaced letters: ", ", ".join(misplace_letters))
    print ("Wrong letters: ",", ".join(wrong_letters))

