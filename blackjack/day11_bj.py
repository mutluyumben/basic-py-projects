# BLACKJACK GAME
import random 

cards = [2, 3, 4, 5, 6 ,7 ,8 ,9 , 10, 10, 10, 10, 11] * 4  
# print(logo)
def comp_hit_or_stand(hand):
    if  sum(hand) < 17:
        return "hit"
    elif  sum(hand) >= 17:
        return "stand"
    else:
        print("ERROR c_HOS!")

def user_hit_or_stand(hand):
    choice = input("HIT OR STAND\n1-HIT\n2-STAND\n")
    if  choice == '1':
        return "hit"
    elif  choice == '2':
        return "stand"
    else:
        print("ERROR u_HOS!")

def take_card(user):
    if user < 11:
        return cards[random.choice(cards)]
    elif  user > 10 and user <= 21:
        return cards[random.choice(cards - cards[0])]
    
def calc(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def comp_hit_or_stand(hand):
    if  sum(hand) < 17:
        return "hit"
    elif  sum(hand) >= 17:
        return "stand"
    else:
        print("ERROR c_HOS!")

def user_hit_or_stand(hand):
    choice = input("HIT OR STAND\n1-HIT\n2-STAND\n")
    if  choice == '1':
        return "hit"
    elif  choice == '2':
        return "stand"
    else:
        print("ERROR u_HOS!")

def take_card(user):
    if user < 11:
        return cards[random.choice(cards)]
    elif  user > 10 and user <= 21:
        return cards[random.choice(cards - cards[-1])]
    
def calc(sum):
    total = sum(sum)
    ace = sum.count(11)
    




user = []
comp = []
turns = []
cartable = False

for turn in range(0, 2):

    user.append(take_card(user))
    comp.append(take_card(user))
    user.append(take_card(user))
    comp.append(take_card(user))

    if user == 21:
        print("User Win")
        break
    elif comp == 21:
        print("Comp Win")
        break
    else:
        cartable == True
            
if cartable == True:
    while cartable is True:
        carden = input(("HIT OR STAND\n1-y\n2-n\n"))
        if carden == '1':
            user.append(take_card())
        elif carden == 'n':             
            turns.append('stand')
            break


while comp_hit_or_stand() != "stand" :
    comp.append(take_card())

       

    

print(f"\nYour hand: {user}\nComputer's hand: {comp}")









