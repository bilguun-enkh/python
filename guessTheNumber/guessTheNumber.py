import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if (guess < random_number):
            print("The number you have guessed is too low!")
        elif (guess > random_number):
            print("The number you have guessed is too high!")
    print(f"You have correctly guessed the number {random_number} Congrats!")
guess(10)