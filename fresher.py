import random

random_number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 to 100: "))

    if guess == random_number:
        print("Congrats! You guessed the number!")
        break
    elif guess < random_number:
        print("Too low! Try again.")
        if guess >= random_number - 10:
            print("You're getting close")
    else:
        print("Too high! Try again.")
        if guess > random_number + 10:
            print("You're getting close!")