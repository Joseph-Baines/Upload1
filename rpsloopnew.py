import random
player_wins = 0
computer_wins = 0
win_score = 3

while player_wins < win_score and computer_wins < win_score:
    print(f'Your wins: {player_wins}\nComputer wins: {computer_wins}')
    rand_num = random.randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print("Rock...\nPaper...\nScissors...\n")

    player1 = input("Player, make your move!\n").lower()
    if player1 == "quit" or player1 == 'q':
            break

    if player1 == computer:
        print("\nIt's a draw!")
    elif player1 == "rock":
        if computer == "scissors":
            print("\nComputer picked scissors... You won!")
            player_wins += 1
        elif computer == "paper":
            print("\nComputer picked paper... You lost!")
            computer_wins += 1
    elif player1 == "paper":
        if computer == "rock":
            print("\nComputer picked rock... You won!")
            player_wins += 1
        elif computer == "scissors":
            print("\nComputer picked scissors... You lost!")
            computer_wins += 1
    elif player1 == "scissors":
        if computer == "paper":
            print("\nComputer picked paper... You win!")
            player_wins += 1
        elif computer == "rock":
            print("\nComputer picked rock... You lost!")
            computer_wins += 1
    else:
        print("\nSomething went wrong. Please type 'rock', 'paper', or 'scissors'.")

if player_wins > computer_wins:
    print("Congratulations, you won!")
elif player_wins == computer_wins:
    print("It's a tie!")
else:
    print("Uh oh!  You lost!")
print(f'Final Score: Your wins: {player_wins} Computer wins: {computer_wins}')
