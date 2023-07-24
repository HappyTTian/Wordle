import pathlib
import random
from string import ascii_letters
from rich.console import Console

console = Console()
console.print("hello [bold red]rich[/] :snake: ")

def refresh(headline):
    console.clear()
    console.rule(f"[bold red] :leafy_green: {headline} :leafy_green: [/] \n")

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
def display_guess (guess_list, answer):
    """Show the user's guess on the terminal and classify all letters.
    """

    # correct_letters = {c1 for c1,c2 in zip(answer,guess) if c1 == c2}
    # misplace_letters = set(answer) & set(guess) - correct_letters
    # wrong_letters = set(guess) - set(answer)
    # print ("Correct letters: ", ", ".join(correct_letters))
    # print ("Misplaced letters: ", ", ".join(misplace_letters))
    # print ("Wrong letters: ",", ".join(wrong_letters))

    for guess in guess_list:
        styles_letters = []
        for letter, correct in zip(guess,answer):
            if letter == correct:
                style = "bold white on green"
            elif letter in answer:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styles_letters.append(f"[{style}]{letter}[/]")
        console.print("".join(styles_letters),justify="center")

def game_over (word):
    print (f"The word was {word}")

def main():
    answer = get_random_word("/home/kool/Wordle/wordList.txt")
    guess_list = ["_"*5]*6

    for i in range(6):
        refresh(headline=f"Guess{i+1}")
        display_guess(guess_list,answer)
        guess_list[i] = input(f"\nGuess {i+1}: ").lower()
        
        if guess_list[i] == answer:
            print ("Correct")
            break
    else:
        game_over(answer)
   

if __name__ == "__main__":
    main()


