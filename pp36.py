import random
secret_number=random.randint(1,10)
guess=0
print("Welcome to the number Guessing Game!")
print("Guess a number between 1 and 10.")
while guess!=secret_number:
    guess=int(input("Enter your guess"))
    if guess<secret_number:
        print("Too Low! Try a higher number.")
    elif guess>secret_number:
        print("Too High! Try a lower number")
    else:
        print("Congratulation! You guessed it right!")
