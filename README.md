# Coffee_Machine  

# Python Coffee Machine

This is a simple coffee machine simulation written in Python. The program allows users to order different types of coffee, insert coins, and receive their chosen beverage if enough resources and money are provided. The machine also provides functionality to check the status of resources and turn off the machine.

## Features

- **Order Coffee**: Choose between espresso, latte, and cappuccino.
- **Insert Coins**: Input the number of coins to pay for the selected coffee.
- **Resource Management**: The machine tracks available resources (water, milk, coffee).
- **Transaction Handling**: Validates if the inserted money is sufficient and returns change if necessary.
- **Reports**: Print a report of the current resources and money collected.
- **Turn Off**: Option to turn off the coffee machine.

## Program Structure

- `coffee_machine.py`: Main script that contains the coffee machine logic.
- `art.py`: Contains the ASCII art logo for the coffee machine.

## Resources
- The resources dictionary keeps track of the current amount of ingredients available in the machine.
  
- resources = {
    "water": 10000,
    "milk": 5000,
    "coffee": 500,
}

## Functions
- **print_report(resources)**: Prints the current resources and money.
- **insert_coins()**: Prompts the user to insert coins and returns the total amount inserted.
- **is_sufficient(order_resources, resources)**: Checks if there are enough resources to make the selected coffee.
- **is_transaction_successful(total_cost, total_money)**: Checks if the inserted money is sufficient for the selected coffee.
- **change_after_payment(total_money)**: Returns the change to the user if any.
- **make_coffee(order_resources, resources)**: Deducts the used resources from the available resources.

## Running the Coffee Machine
- The **start_coffee_machine()** function starts the coffee machine and handles user interactions.

## Example Interaction

Welcome to the Python Coffee Machine
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many 1 rupee coins?: 0
How many 2 rupee coins?: 0
How many 5 rupee coins?: 10
How many 10 rupee coins?: 0
How many 20 rupee coins?: 0
Here is 0 rupees in change.
Here is your latte. Enjoy!

What would you like? (espresso/latte/cappuccino): report
water: 9800
milk: 4850
coffee: 476
Money: 50

