MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 20,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 100,
    }
}

resources = {
    "water": 10000,
    "milk": 5000,
    "coffee": 500,
}
money = 0

def print_report(resources):
    """PRINT THE AMOUNT OF RESOURCES AVAILABLE IN THE MACHINE"""
    for key in resources:
        print(f"{key}: {resources[key]}")
    print(f"Money: {money}")

def insert_coins():
    """FUNCTION TO TAKE MONEY FROM CUSTOMER"""
    try:
        print("Please insert coins.")
        one = int(input("How many 1 rupee coins?: "))
        two = int(input("How many 2 rupee coins?: "))
        five = int(input("How many 5 rupee coins?: "))
        ten = int(input("How many 10 rupee coins?: "))
        twenty = int(input("How many 20 rupee coins?: "))
    except ValueError:
        print("Invalid input. please enter integer values.")
        return 0
    return one + (2 * two) + (5 * five) + (10 * ten) + (20 * twenty)

def is_sufficient(order_resources,resources):
    """ CHECK IF THERE ARE SUFFICIENT RESOURCES AVAILABLE TO PROCESS THE ORDER"""
    for key in order_resources:
        if resources[key] < order_resources[key]:
            print(f"Sorry there is not enough {key}.\n")
            return False
    return True

def is_transaction_successful(total_cost, total_money):
    """CHECK WHETHER TRANSACTION IS SUCCESSFUL OR NOT"""
    if total_cost > total_money:
        print("Sorry that's not enough money. Money Refunded.\n")
        return False
    return True

def change_after_payment(total_money):
    """PRINT TOTAL CHANGE IF THERE IS ANY TO BE RETURNED TO CUSTOMER"""
    if total_money > 0:
        print(f"Here is {total_money} rupees in change.")

def make_coffee(order_resources,resources):
    """DEDUCT THE AMOUNT OF RESOURCES REQUIRED TO MAKE ORDER FROM THE AVAILABLE RESOURCES"""
    for key in order_resources:
        resources[key] -= order_resources[key]

from art import logo

def start_coffee_machine():
    off = False
    print(logo)
    while not off:
        print("Welcome to the Python Coffee Machine")
        # TODO: 1 PROMPT INPUT
        prompt = input("What would you like? (espresso/latte/cappuccino): ")

        # TODO: 2 PRINT REPORT
        if prompt == "report":
            print_report()

        elif prompt == "off":
            off = True

        elif prompt in MENU:
            # TODO: 3 CHECK RESOURCES SUFFICIENT
            order_resources = MENU[prompt]["ingredients"]
            sufficient = is_sufficient(order_resources, resources)

            # TODO: 4 PROCESS COINS
            if sufficient:
                total_money = insert_coins()

            # TODO: 5 CHECK TRANSACTION SUCCESSFUL
                total_cost = MENU[prompt]["cost"]

                success = is_transaction_successful(total_cost, total_money)
                if success:
                    total_money -= total_cost
                    change_after_payment(total_money)

                    # TODO: 6 MAKE COFFEE
                    global money
                    money += total_cost
                    make_coffee(order_resources, resources)
                    print(f"Here is your {prompt}. Enjoy!\n")

        else:
            print("Invalid selection. Please choose from the available options.")

start_coffee_machine()