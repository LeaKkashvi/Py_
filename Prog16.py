#Rock Paper Scissors Game – Determine winner between user and computer

import random
choices = ["rock", "paper", "scissors"]
u= input("Enter your choice (rock, paper, scissors): ").lower()

c = random.choice(choices)
print("Computer chose:", c)
if u == c:
    print("It's a tie!")
elif (u == "rock" and c == "scissors") or (u == "paper" and c == "rock") or (u == "scissors" and c == "paper"):
    print("You win!")
else:
    print("Computer wins!")
    
