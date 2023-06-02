# Number Guesser
# Author: Nathan Zou
# This program is a simple guessing game where the player tries to guess a randomly generated secret number.
# The player has a limited number of guesses to find the correct number within a given range.
# After each guess, the program provides feedback to help the player adjust their subsequent guesses.
# If the player guesses the correct number, they win and the program congratulates them.
# If the player runs out of guesses, they lose and the program reveals the secret number.

import random

def playGame():
    # Generate a random secret number
    secretNumber = random.randint(1, 100)
    # Set the maximum number of guesses
    maxGuesses = 10

    print("=== Welcome to the Guessing Game! ===")
    print("I'm thinking of a number between 1 and 100.")
    print("You have", maxGuesses, "guesses to find the number.")

    # Game loop
    guessCount = 0
    while True:
        # Get user's guess
        guess = int(input("Enter your guess (1-100): "))
        guessCount += 1

        # Check if the guess is correct
        if guess == secretNumber:
            print("Congratulations! You guessed the secret number:", secretNumber)
            print("It took you", guessCount, "guesses.")
            break
        elif guess < secretNumber:
            print("Too low!")
        else:
            print("Too high!")

        # Check if the user has run out of guesses
        if guessCount == maxGuesses:
            print("Sorry, you ran out of guesses!")
            print("The secret number was:", secretNumber)
            break

    # Ask the user if they want to play again
    playAgain = input("Do you want to play again? (yes/no): ")
    if playAgain.lower() == "yes":
        print("\n====================================\n")
        playGame()
    else:
        print("Thank you for playing!")

# Start the game
playGame()
