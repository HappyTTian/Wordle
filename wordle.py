import pathlib
import random
import contextlib
from string import ascii_letters,ascii_lowercase
from rich.console import Console
from rich.theme import Theme


console = Console(theme = Theme({"warning":"red on yellow"}))
console.print("hello [bold red]rich[/] :snake: ")

NUM_GUESS=6
WORD_LEN=5 #the length of word we guess

def refresh(headline):
    console.clear()
    console.rule(f"[bold red] :leafy_green: {headline} :leafy_green: [/] \n")

def get_random_word(file):

    words = [
        word.lower()
        for word in pathlib.Path(file).read_text(encoding="utf-8").strip().split('\n')
        if len(word) == WORD_LEN and all(letter in ascii_letters for letter in word)
    ]
    #check if length is empty
    if len(words) != 0:
        answer = random.choice(words)
        return answer
    else:
        console.print(f"There is no words of length {WORD_LEN}", style="warning")
        raise SystemExit()


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

    alphabets = {letter:letter for letter in ascii_lowercase}

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
            if letter != '_':
                alphabets[letter] = f"[{style}]{letter}[/]"
        console.print("".join(styles_letters),justify="center")
        
    console.print("\n"+"".join(alphabets.values()),justify="center")


def game_over (guess_list,answer,guess_correct):
    refresh(headline="Game over")
    display_guess(guess_list,answer)
    if guess_correct:
        console.print(f"[bold red]You win! The answer is [/] {answer}[/] ")
    else:
        console.print(f"[bold red]You lose! The answer is[/] [bold green]{answer}[/] ")

def guess_word(prev_words):
    
    while 1:
        guess = input(f"\nGuess {len(prev_words)+1}: ").lower()
        if guess in prev_words:
            console.print(f"You've already guessed {guess}",style="warning")
            continue
        elif len(guess) != WORD_LEN:
            console.print("The length of the word is not 5",style="warning")
            continue
        elif any((invalid := letter) not in ascii_letters for letter in guess):
            console.print(
                f"Invalid letter: '{invalid}'.Only English letters are allowed",
                style = "warning"
            )
            continue
        else:
            return guess
    

def main():
    answer = get_random_word("/home/kool/Wordle/wordList.txt")
    guess_list = ["_"*WORD_LEN]*NUM_GUESS
    guess_correct = 0
    with contextlib.suppress(KeyboardInterrupt):
        for i in range(NUM_GUESS):
            refresh(headline=f"Guess{i+1}")
            display_guess(guess_list,answer)
            guess_list[i] = guess_word(prev_words=guess_list[:i])
            
            if guess_list[i] == answer:
                guess_correct = 1
                print ("Correct")
                break
    
    
    game_over(guess_list,answer,guess_correct)
   

if __name__ == "__main__":
    main()


