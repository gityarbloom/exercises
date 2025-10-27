

def init_state(secret: str, max_tries: int):
    display = []
    for sign in secret:
        display.append("_")
    game_dict = {
                "secret": secret, 
                "display": display, 
                "guessed": set(), 
                "wrong_guesses": 0, 
                "max_tries": max_tries
                }
    return game_dict


def validate_guess(ch: str, guessed: set[str]):
    if ch not in guessed and len(ch) == 1 and ch.isalpha():
        return True, "the guess is proper"
    return False, "the guess can be only an one Alphbet letter"



def apply_guess(state: dict, ch: str):
    flag_check = validate_guess(ch, state["guessed"])
    if flag_check[0]:
        if ch in state["secret"]:
            indexes = []
            for i in range(len(state["secret"])):
                if state["secret"][i] == ch:
                    indexes.append(i)
            for index in indexes:
                state["display"][index] = ch
            state["guessed"].add(ch)
            return True
        state["guessed"].add(ch)
        state["wrong_guesses"] += 1
        return False
    return False



def is_won(state: dict):
    bool_flag = False
    for i in range(len(state["secret"])):
        if state["display"][i] != state["secret"][i]:
            bool_flag = False
    return bool_flag


def is_lost(state: dict):
    if len(state["guessed"]) >= state["max_tries"]:
        return True

def render_display(state: dict):
    show_string = "".join(state["display"])
    return show_string


def render_summary(state: dict):
    end_present = f"\n***************** \nthe secret word was:  {state["secret"]} \n***************** \nthe letters you guessed they: , {state["guessed"]}"
    return end_present


# game_dict = init_state("abad", 10)
# print(game_dict)
# one_round = apply_guess(game_dict, "a")
# one_round = apply_guess(game_dict, "b")
# one_round = apply_guess(game_dict, "a")
# # one_round = apply_guess(game_dict, "d")
# print(one_round)
# print(game_dict)
# print(is_won(game_dict))
# print(render_display(game_dict))
# print(render_summary(game_dict))