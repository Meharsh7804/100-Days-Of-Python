# Write a Python program that simulates a simple guessing game. The program generates a random number, and the user has to guess the number. It should provide feedback to the user (e.g., "Too low" or "Too high") and continue until the user guesses the correct number.

# Program to generate a random number between 0 and 50

import random
print("===================WELCOME TO THIS GUESSING GAME===================")

number = random.randint(0,50)
print(number)
attempts = 0
guess = 0
while(guess != number):
    guess = int(input("Guess the number "))
    attempts += 1
    if(guess > number):
        print("Too High....try again ")
    elif(guess < number):
        print("Too Low....try again ")
    else:
        ("BRAVO, that's right....the number is ",number)
        ("You got it in ",attempts," attempts")

print("===================HAVE A NICE DAY===================")
