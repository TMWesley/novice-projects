from random import randint

#create a list of play options
t = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False

player = True

while player == True:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    else:
        print("That's not a valid play, please check your spelling")
    player == False
    computer = t[randint(0,2)]
