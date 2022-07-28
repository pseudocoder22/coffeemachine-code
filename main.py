MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
# separate ya
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1. ask the user what what customer likes

# TODO 1.1 resources and money
menu = MENU["cappuccino"]['cost']

req_coffee = MENU['cappuccino']['ingredients']['water']


# TODO 2. insert coins, quarters,  dimes , nickels, pennies,
# TODO 2.1 total for each drink
# TODO 2.2 give change

money = 0
def payment(type_of_drink):
    global money
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (0.25 * quarters) + (0.10 * dimes) + (0.01 * pennies ) + (0.05 * nickels)
    cost = MENU[type_of_drink]["cost"]
    change = total - cost
    print(f"your total {total}")
    print(f"drink cost: {cost}")
    if total < cost:
        print("Sorry not enough")
    elif total > cost:
        money += cost
        print(f"Your change: {change}")
        print(f"Money: {money}")
    elif total == cost:
        print(0)

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']


def drink(type_of_drink):
    global water
    global milk
    global coffee

    if type_of_drink == 'espresso':
        req_milk = 0
    else:
        req_milk = MENU[type_of_drink]['ingredients']['milk']

    req_coffee = MENU[type_of_drink]['ingredients']['coffee']
    req_water = MENU[type_of_drink]['ingredients']['water']

    if type_of_drink == 'espresso':
        water -= req_water
        coffee -= req_coffee

    else:
        water -= req_water
        milk -= req_milk
        coffee -= req_coffee
    print(f"Here's your {type_of_drink}")

# TODO 3. print report

def report():
    print(f"water: {water}")
    print(f"milk: {milk}")
    print(f"coffee {coffee}")
    order = False
    return order

# TODO 4. creating a function that checks if there is enough
# print(MENU["cappuccino"]['cost']) - to access dic within a dic


def checker(type_of_drink):
    if water < MENU[type_of_drink]['ingredients']['water']:
        print("Sorry there is not enough water")
    elif type_of_drink == "latte" and milk < MENU[type_of_drink]['ingredients']['milk']:
        print('Sorry there is not enough milk')
    elif  type_of_drink == "cappuccino" and milk < MENU[type_of_drink]['ingredients']['milk']:
        print('Sorry there is not enough milk')
    elif coffee < MENU[type_of_drink]['ingredients']['coffee']:
        print("Sorry there is not enough milk")
    else:
        payment(type_of_drink)
        drink(type_of_drink)


# TODO 4. repeat. Creating while loop

order = True

while order:
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    if ask == "report":
        report()
    elif ask =="stop":
        order = False
    else:
        checker(ask)


