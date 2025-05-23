import random

"""Juego del ahorcado donde el jugador debe adivinar una palabra letra por letra."""

word_list = ["apple", "elderberry", "fight", "guitar", "house", "mango", "nurse", "orange", "penguin", "queen", "rabbit", "snake", "tiger", "umbrella", "vulture", "watermelon", "xylophone", "yacht", "zebra"]

def create_blank_spaces(word) -> str:
    """Crea una cadena de guiones bajos del mismo largo que la palabra."""
    return "_" * len(word)

def complete_word_replacing_blank_spaces(word, guess, blank_spaces) -> str:
    """Reemplaza los espacios en blanco con la letra adivinada en las posiciones correctas."""
    letter_location = [i for i, char in enumerate(word) if char == guess]
    for letter in letter_location:
        if letter_location == len(word):
            blank_spaces = blank_spaces[:letter] + guess
        else:
            blank_spaces = blank_spaces[:letter] + guess + blank_spaces[(letter+1):]
    return blank_spaces


def main():
    """Función principal que ejecuta el juego del ahorcado."""
    lives = 6
    chosen_word = random.choice(word_list)
    blank_spaces = create_blank_spaces(chosen_word)
    end_game = False
    while not end_game:
        print(f"*********Guess a letter in the word: (currently: {blank_spaces})*********")
        guess = input().lower()
        if guess in chosen_word:
            print("****************Correct!****************")
            blank_spaces = complete_word_replacing_blank_spaces(chosen_word, guess, blank_spaces)
            if "_" not in blank_spaces:
                print("****************You win!****************")
                end_game = True
                break
        else:
            lives -= 1
            print(f"****************Incorrect! {lives} lives left****************")
            if lives == 0:
                print("****************You lose!****************")
                end_game = True
                break
 
if __name__ == "__main__":
    main()