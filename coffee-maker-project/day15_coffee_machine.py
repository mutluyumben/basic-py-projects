from day15_coffe_machine_data import MENU, resources
import string

def coffee_espresso():
    water_req = MENU["espresso"]["ingredients"]["water"]
    coffee_req = MENU["espresso"]["ingredients"]["coffee"]

    if resources["water"] < water_req:
        return "Error: not enough water to make espresso"
    
    elif resources["coffee"] < coffee_req:
        return "Error: not enough coffe to make espresso"
    
    resources["water"] -= water_req
    resources["coffee"] -= coffee_req
    return print("Please Continue")

def coffee_latte():
    water_req = MENU["latte"]["ingredients"]["water"]
    coffee_req = MENU["latte"]["ingredients"]["coffee"]

    if resources["water"] < water_req:
        return "Error: not enough water to make latte"
    
    elif resources["coffee"] < coffee_req:
        return "Error: not enough coffe to make latte"
    
    resources["water"] -= water_req
    resources["coffee"] -= coffee_req
    return print("Please Continue")

def coffee_cappucino():
    water_req = MENU["cappucino"]["ingredients"]["water"]
    coffee_req = MENU["cappucino"]["ingredients"]["coffee"]

    if resources["water"] < water_req:
        return "Error: not enough water to make cappucino"
    
    elif resources["coffee"] < coffee_req:
        return "Error: not enough coffe to make cappucino"
    
    resources["water"] -= water_req
    resources["coffee"] -= coffee_req
    return print("Please Continue")

def coffee_coin():
    Penny = 0.01
    money_Penny = int(input("How much Penny do you want to insert: "))
    Nickel = 0.05
    money_Nickel = int(input("How much Nickel do you want to insert: "))
    Dime = 0.010
    money_Dime = int(input("How much Dime do you want to insert: "))
    Quarter = 0.25
    money_Quarter = int(input("How much Quarter do you want to insert: "))
    
    total_penny = Penny * money_Penny
    total_Nickel = Nickel * money_Nickel
    total_Dime = Dime * money_Dime
    total_Quarter = Quarter * money_Quarter
    total_money = total_penny + total_Nickel + total_Dime + total_Quarter
    
    return total_money


is_ON = True
choice = input("Which coffee do you want to drink?\n1-Espresso\n2-Latte\n3-Cappuccino : ")

while is_ON:
    if choice == 'off':
        is_ON = False

    elif choice == "report":
        print(f"Water:  {resources['water']}")
        print(f"Milk:   {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")

    elif  choice == "1":
        coffee_espresso()

        total_money = coffee_coin()
        if total_money >= MENU["espresso"]["cost"]:
            charge_money = total_money - MENU["espresso"]["cost"]
            print(f"Here is your charge: {charge_money}")
            print("Here is your coffee: ☕")
        elif total_money  <  MENU["espresso"]["cost"]:
            print("Coin is not enough!")
        else:
            print("ERROR(es_else)")

    elif choice == '2':
        coffee_latte()
        
        total_money = coffee_coin()
        if total_money >= MENU["latte"]["cost"]:
            charge_money = total_money - MENU["latte"]["cost"]
            print(f"Here is your charge: {charge_money}")
            print("Here is your coffee: ☕")
        elif total_money  <  MENU["latte"]["cost"]:
            print("Coin is not enough!")
        else:
            print("ERROR(es_else)")

    elif choice == '3':
        coffee_cappucino()
        
        total_money = coffee_coin()
        if total_money >= MENU["cappucino"]["cost"]:
            charge_money = total_money - MENU["cappucino"]["cost"]
            print(f"Here is your charge: {charge_money}")
            print("Here is your coffee: ☕")
        elif total_money  <  MENU["cappucino"]["cost"]:
            print("Coin is not enough!")
        else:
            print("ERROR(es_else)")

    else: 
        print("ERROR(coffee_choice)")
