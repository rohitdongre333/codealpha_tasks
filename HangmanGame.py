import random

words = ["apple", "tiger", "house", "table", "plant"]

secret_word = random.choice(words)

guessed_word = ["_"] * len(secret_word)

wrong_guesses = 0
max_wrong = 6

while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))

    letter = input("Enter a letter: ")

    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                guessed_word[i] = letter
        print("Correct!")

    else:
        wrong_guesses += 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("You Win!")
else:
    print("You Lose! Word was:", secret_word)