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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredient):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for items in order_ingredient:
        if order_ingredients[item] >= resources[item]:
            print("sorry, there is not enough water{item}.")
            return false
    return True


def process_coins():
    """Returns the total calculated coins from coins inserted. """
    print("Please insert a coin.")
    total = object = int(input("how many Quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.01
    total += int(input("how many pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if the money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is &{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refund.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources. """
    for item in order_ingredients:
        resources [item] -= order_ingredients[item]
    print(f"Here is your{drink_name}☕")


is_on = True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "Off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredient"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

