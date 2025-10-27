from hangman.game import is_won, is_lost, render_summary, render_display

def prompt_guess():
    guessing = str(input("enter your guessing: "))
    return guessing


def print_status(state: dict):
    remaining_attemps = state["max_tries"] - len(state["guessed"])
    print(f"guess_status is: , {render_display(state)}, \nguessed letters: , {state["guessed"]}, \nremaining guesses: , {remaining_attemps}")
    
    
def print_result(state: dict):
    if is_won(state):
        print("congratulations! you won")
        print(render_summary(state))
    elif is_lost(state):
        print("game is over, you lost")
        print(render_summary(state))

