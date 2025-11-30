import random

try:
    low = int(input('Enter the lower bound \n'))
    high = int(input('Enter higher bound \n'))
except:
    print("Please enter a valid number")

r = random.randint(low, high)

guess_count=5

while guess_count>0:
    try:
        new_guess_str = input(f'remani guess: {guess_count} => Entter your guess \n')
        new_guess = int(new_guess_str)

        if r == new_guess:
            print("your guess is correct, you win \n")
            break
        elif r > new_guess:
            print(f"{new_guess} is lower than selected number")
        else:
            print(f"{new_guess} is higher than selected number")

        guess_count -=1
    except:
        print("Please enter a valid number \n")