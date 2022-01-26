import random
from turtle import clear
from wordlistfile import word_list
game_is_finished = False
lives = 5
word = random.choice(word_list)
Trial = []
for letter in word:
    Trial.append("_")
while not game_is_finished:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in Trial:              # nice!!!!
        print(f"You've already guessed {guess}")
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            Trial[position] = letter
    print(f"{' '.join(Trial)}")            # whaaaat??
    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if "_" not in Trial:
        game_is_finished = True
        print("You win.")
