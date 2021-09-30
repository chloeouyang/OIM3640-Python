import random

secret_number = random.randint(1, 20)
a = input("Hello! What is your name?")
print(f"Well,{a},I am thinking of a number between 1 and 20.")

guess = 0
tries = 0
n = 6


while guess != secret_number and tries < n:
    guess = int(input("Take a guess."))
    if guess > secret_number:
        print("Your guess is too high.")
        tries = tries + 1

    elif guess < secret_number:
        print("Your guess is too low.")
        tries = tries + 1

    elif guess == secret_number:
        tries = tries + 1
        print(f"Good job,{a}!You guessed my number in {tries} guesses!")

if tries == n:
    print("You are out of tries. Better luck next time.")
