print("Welcome to my Casino- \n - Who guess the secret number between 0-100 - ")
secret = str(65)
print()
guess = -1

while guess != secret:
    guess = input('Guess the secret number:')
    if guess == secret:
        print("You got it - \n  !!! You get the Jackpot !!!!")
    elif guess < secret:
        print(" The Secret number is bigger")
    elif guess > secret:
        print(" The Secret number is smaller")
