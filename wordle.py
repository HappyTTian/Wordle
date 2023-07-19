import pathlib
import random
from string import ascii_letters

#get a random word for the game
def get_random_word(file):
    word_length = 5 #the length of word we guess

    words = [
        word.lower()
        for word in pathlib.Path(file).read_text(encoding="utf-8").strip().split('\n')
        if len(word) == word_length and all(letter in ascii_letters for letter in word)
    ]
    answer = random.choice(words)
    print(answer)
    return answer

#show which letters are guessed right and which are wrong
def display_guess (guess, answer):
    """Show the user's guess on the terminal and classify all letters.

    ## Example:

    >>> display_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R
    """

    correct_letters = {c1 for c1,c2 in zip(answer,guess) if c1 == c2}
    misplace_letters = set(answer) & set(guess) - correct_letters
    wrong_letters = set(guess) - set(answer)
    print ("Correct letters: ", ", ".join(correct_letters))
    print ("Misplaced letters: ", ", ".join(misplace_letters))
    print ("Wrong letters: ",", ".join(wrong_letters))

def game_over (word):
    print (f"The word was {word}")

def main():
    answer = get_random_word("wordList.txt")
    for i in range(6):
        guess = input(f"Guess {i+1}: ").lower()
        if guess == answer:
            print ("Correct")
            break
        display_guess(guess,answer)
    else:
        game_over(answer)
   

if __name__ == "__main__":
    main()


