import random
import time
print("Before Playing the Game Winning Rules are as follows:\n"
        + "Rock vs paper-> paper wins \n"
        + "Rock vs scissor-> Rock wins \n"
        + "paper vs scissor-> scissor wins. \n")
print("Entering Choice \n"
     + "1 For Rock \n"
     + "2 For Paper \n"
     + "3 For Scissor \n")
while True:
    print("Now it's User Turn")
    UsersChoice = int(input("Enter Your choice 1:Rock 2:Paper 3:Scissor\n"))
    while UsersChoice > 3 or UsersChoice < 1:
        UsersChoice = int(input("Please Enter Correcct One ! \n"))
    if UsersChoice == 1:
        print("You Selected Rock")
    elif UsersChoice == 2:
        print("You Selected Paper")
    else:
        print("You Selected Scissor")
        
    print("Now it's Computer's Turn")
    possible_actions = [1,2,3]
    ComputerChoice = random.choice(possible_actions)
    if ComputerChoice == 1:
        print("Computer Selected Rock \n")
    elif ComputerChoice == 2:
        print("Computer Selected Paper \n")
    else:
        print("Computer Selected Scissor \n")
    
    if UsersChoice == ComputerChoice:
        time.sleep(2)
        print("----- And the Result is----- \n")
        print("Tie")
    elif UsersChoice == 1: 
        if ComputerChoice == 2:
            time.sleep(2)
            print("----- And the Result is----- \n")
            print("Wins by PC")
        else:
            time.sleep(2)
            print("----- And the Result is----- \n")
            print("Wins by User")

    elif UsersChoice == 1:
        if ComputerChoice == 3:
            time.sleep(2)
            print("----- And the Result is----- \n")
            print("Wins by User")
        else:
            time.sleep(2)
            print("----- And the Result is----- \n")
            print("Wins PC")
    elif UsersChoice == 2:
        if ComputerChoice == 3:
            time.sleep(2)
            print("----- And the Result is----- \n")
            print("Wins by PC")
        else:
            time.sleep(2)
            print("----- And the Result is----- \n")
            print("Wins User")
    
    print("-------------------------------------")
    
    playerinput = input("Do you want to play y/n? \n")
    if(playerinput == 'n'):
        break

print("Thanks for playing")
