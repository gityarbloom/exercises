from hangman.data import *
from hangman.game import init_state, apply_guess
from hangman.words import *
from hangman.io import *

def play(words: list[str]):
    secret = choose_secret_word(words)
    max_tries = len(secret) * 2
    state = init_state(secret, max_tries)
    while not is_won(state) and not is_lost(state):
        print_status(state)
        guessed = apply_guess(state, prompt_guess())
        print("\n*********** \ncorrect guess! \n*********** \n" if guessed else "\n*********** \nwrong guess... \n*********** \n")
    print_result(state)

if __name__ == "__main__":
    play(words)