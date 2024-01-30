import random
secret_number = random.randint(1, 10)
guesses = 0

while guesses <= 5:
    guess = int(input("Guess a number between 1 to 10: "))
    guesses += 1

    if guess == secret_number:
        print("Congrats you guessed the correct number")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if guess != secret_number:
    print("Sorry, you ran out of guesses. The number was ", secret_number)