import random

word_list = ["apples", "bananas", "oranges", "grapes", "pears", "strawberries"]
chosen_word = random.choice(word_list)

display = ['_' for _ in chosen_word]
end_of_game = False
guessed_letters = set()

def update_display(letter):
    global display
    for i, char in enumerate(chosen_word):
        if char == letter:
            display[i] = letter

def print_display():
    print(' '.join(display))

def game_over():
    global end_of_game
    if '_' not in display:
        end_of_game = True
        print("You win")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
    elif guess in guessed_letters:
        print("You've already guessed that letter.")
    else:
        guessed_letters.add(guess)
        update_display(guess)
        print_display()
        game_over()
    