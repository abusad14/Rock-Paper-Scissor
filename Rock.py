import random

options = ("rock" , "paper" , "scissor")
player = None
print()

while True:
    options = ("rock" , "paper" , "scissor")
    player = None
    print()
    while player not in options:
        player = input("Enter your choice (rock , paper , scissor) :").lower()
        computer = random.choice(options)
        print()

    print(f"Your choice :- {player}")
    print(f"Computer choice :- {computer}")
    print()

    if (player == computer ):
        print("---It's a Tie---")
    elif(player == "rock" and computer == "paper"):
        print("--- Oops!! You LOSE :( ---")

    elif(player == "paper" and computer == "scissor"):
        print("--- Oops!! You LOSE :( ---")
    elif(player == "scissor" and computer == "rock"):
        print("--- Oops!! You LOSE :( ---")
    else:
        print("-- Woohoo!! YOU WIN ---")
           
    play = input("Try Again (yes/no)??")
    if(play == "yes"):
        continue
        
    else:
        print("Game Over")
        break
            
    