# Simple Number Guessing Game
import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("\nI'm thinking of a number between 1 and 100.")
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess == secret_number:
            print(f"You've got it! The number was {secret_number}.")
            print(f"It took you {attempts} attempts to guess the number.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    play_game()
