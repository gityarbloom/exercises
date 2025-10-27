from random import randint

def choose_secret_word(words: list[str]):
    rand_index = randint(0, len(words) - 1)
    return words[rand_index]

# print(choose_secret_word(["a", "b", "c", "d"]))