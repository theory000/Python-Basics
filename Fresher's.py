import random

secret_number = random.randint(1, 10)
guesses = 0

while guesses < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses += 1

    if guess == secret_number:
        print("Congrats! You guessed the number in", guesses, "tries!")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if guess != secret_number:
    print("Sorry, you ran out of guesses. The number was", secret_number)