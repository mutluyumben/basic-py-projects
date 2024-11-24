import random 
from day14_art import logo
from day14_data import data

from day14_art import vs

print(logo)
game_cont = True
score = 0

while game_cont is True: 
    c1 = random.choice(data)
    print(f"Compare A: {c1['name']}, {c1['description']}, from {c1['country']}\n")
    
    print(vs)
    
    c2 = random.choice(data) 
    print(f"Compare B: {c2['name']}, {c2['description']}, from {c2['country']}\n")
    
    choice = input("Who has most follower on Instagram! (A/B)?\n").lower()
    
    if choice == 'a':
        if c1["follower_count"] > c2["follower_count"]:
            print("Correct\n")
            score = score + 1
        elif c2["follower_count"] > c1["follower_count"]:
            print("Incorrect\n")
            break 
        else: 
            print("ERROR: 'a' else\n")
            break
    
    elif choice == 'b':
        if c2["follower_count"] > c1["follower_count"]:
            print("Correct\n")
            score = score + 1
        elif c1["follower_count"] > c2["follower_count"]:
            print("Incorrect\n")
            break
        else :
            print("ERROR: 'b' else\n")
            break
    else:
        print("ERROR! Invalid Input, Please Enter A or B \n")
print(f"Your score is: {score}")
    
    
    
    
    
    




