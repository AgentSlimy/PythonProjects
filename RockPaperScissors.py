# Rock Paper Scissors / Roshambo
# Author: Nathan Zou
# The user will play the classic game of Rock Paper Scissors against the computer.
# The user determines at the beginning of each round the number of points required for a win. The game will continue until either the user or the computer reaches the number of wins set by the user.
# The user will select their move for each round.
# The computer will randomly select its move for each round.
# The winner of each round is determined by: Rock > Scissors > Paper > Rock.
# Scores for both the user and computer will be displayed once the match is concluded.

import random

# Ask the user for their choice (rock, paper, or scissors)
def getUserChoice():
    while True:
        userChoice = input("Enter your choice (rock/paper/scissors): ").lower()
        if userChoice in ['rock', 'paper', 'scissors']:
            return userChoice
        else:
            print("Invalid choice. Please try again.")

# Generate a random choice for the computer (rock, paper, or scissors)
def getComputerChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Determine the winner based on the user and computer choices
def determineWinner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return "It's a tie!"
    elif (userChoice == 'rock' and computerChoice == 'scissors') or \
         (userChoice == 'paper' and computerChoice == 'rock') or \
         (userChoice == 'scissors' and computerChoice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Ask the user if they want to play again
def playAgain():
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == 'yes'

# Main function to play the Rock Paper Scissors game
def playGame():
    print("Welcome to Rock Paper Scissors!")
    name = input("Enter your name: ")
    print(f"Hi, {name}! Let's begin.")

    userScore = 0
    computerScore = 0

    while True:
        print("===================================")
        print("Score:")
        print(f"{name}: {userScore}  Computer: {computerScore}")
        print("===================================")

        pointsRequired = int(input("Enter how many points are required for a win: "))
        print(" ")

        while userScore < pointsRequired and computerScore < pointsRequired:
            userChoice = getUserChoice()
            computerChoice = getComputerChoice()

            print(f"{name} chose {userChoice}.")
            print(f"Computer chose {computerChoice}.")

            result = determineWinner(userChoice, computerChoice)
            print(result)

            if result == "You win!":
                userScore += 1
                print(" ")
            elif result == "Computer wins!":
                computerScore += 1
                taunts = ["Ha! I'm too good!", "Better luck next time!", "You can't beat me!"]
                print("Computer: " , random.choice(taunts))
                print(" ")
            elif result == "It's a tie!":
                print(" ")

        print("===================================")
        print("Final Score:")
        print(f"{name}: {userScore}  Computer: {computerScore}")
        print("===================================")

        if userScore > computerScore:
            print(f"Congratulations, {name}! You won!")
        else:
            print("Sorry, you lost. Better luck next time!")

        if not playAgain():
            break

        # Reset scores for a new game
        userScore = 0
        computerScore = 0

    print("Thank you for playing Rock Paper Scissors!")

playGame()
