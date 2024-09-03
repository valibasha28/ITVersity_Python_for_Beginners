import random
number_to_guess = random.randint(1, 6)

attempts = 0

while True:
    guess = int(input("Guess the number between (1 and 6): "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low, Try again!")
    elif guess > number_to_guess:
        print("Too high, Try again!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break