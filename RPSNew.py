import random
while True:
    rand_num = random.randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print("Rock...\nPaper...\nScissors...\n")

    player1 = input("Player, make your move!\n").lower()

    if player1 == computer:
        print("\nIt's a draw!")
    elif player1 == "rock":
        if computer == "scissors":
            print("\nComputer picked scissors... You won!")
        elif computer == "paper":
            print("\nComputer picked paper... You lost!")
    elif player1 == "paper":
        if computer == "rock":
            print("\nComputer picked rock... You won!")
        elif computer == "scissors":
            print("\nComputer picked scissors... You lost!")
    elif player1 == "scissors":
        if computer == "paper":
            print("\nComputer picked paper... You win!")
        elif computer == "rock":
            print("\nComputer picked rock... You lost!")
    else:
        print("\nSomething went wrong. Please type 'rock', 'paper', or 'scissors'.")