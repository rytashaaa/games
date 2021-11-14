import random

def rockpaperscissors():
    player2 = random.choice(['rock', 'paper', 'scissors'])
    choice = input("Rock, paper, scissors, shoot: ")
    count = 0
    win = 0
    while count < 4:
        player2 = random.choice(['rock', 'paper', 'scissors'])
        if player2 == 'rock':
            print("rock")
            if choice != 'paper':
                choice = input("Rock, paper, scissors, shoot: ")
            elif choice == 'paper':
                win += 1
                choice = input("Rock, paper, scissors, shoot: ")
        if player2 == 'paper':
            print("paper")
            if choice != 'scissors':
                choice = input("Rock, paper, scissors, shoot: ")
            elif choice == 'scissors':
                win += 1
                choice = input("Rock, paper, scissors, shoot: ")
        if player2 == 'scissors':
            print("scissors")
            if choice != 'rock':
                choice = input("Rock, paper, scissors, shoot: ")
            elif choice == 'rock':
                win += 1
                choice = input("Rock, paper, scissors, shoot: ")
        count += 1
        
    print("you won:",win, "times.")
        
rockpaperscissors()
