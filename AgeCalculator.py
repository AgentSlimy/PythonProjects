# Age Calculator
# Author: Nathan Zou
# This program calculates various units of time based on a user's inputted age in years.
# The user is prompted for their name and age, and the program outputs the number
# for a rough estimate of the minutes, days, weeks, and decades they have been alive.

import math

def ageCalculator():
    # Prompts the user for their name and age
    name = input("What is your name? ")
    age = int(input("How old are you in years? (Inputted value must be a number) "))

    # Calculation for the various units of time based on their age.
    minutesAlive = age * 365 * 24 * 60
    daysAlive = age * 365
    weeksAlive = age * 52
    if age % 10 >= 5: # Based on the inputted years, will round up or down to the nearest 10
        decadesAlive = math.ceil(age / 10)
    else:
        decadesAlive = math.floor(age / 10)
    
    # Displays results
    print(f"\nHello, {name}!")
    print("You have been alive for roughly:")
    print(f" {minutesAlive:,} minutes, or")
    print(f" {daysAlive:,} days, or")
    print(f" {weeksAlive:,} weeks, or")
    print(f" {decadesAlive} decade(s).")

# Main program loop
while True:
    ageCalculator()
    repeat = input("\nDo you want to calculate another person's age? (yes/no): ")
    if repeat.lower() != "yes":
        break
