from random import randint

random_number = randint(1,10)
guess = None
while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess == random_number:
        print(f"You are correct, the number is {random_number}!  You win!")
        play = str(input("Would you like to play again?  (y/n)"))
        if play == "y":
            random_number = randint(1, 10)
            guess = None
        else:
            print("Thank you for playing!  Have a great day!")
            break
    elif guess < random_number:
        print("Your guess is too low... Try again!")
    elif guess > random_number:
        print("Your guess is too high... Try again!")
    else:
        print("Please enter a number from 1 to 10.")