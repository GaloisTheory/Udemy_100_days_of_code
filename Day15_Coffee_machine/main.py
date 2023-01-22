from abc import ABC


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

TYPES_OF_COINS = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}


class coffee_machine(ABC):
    def __init__(self):
        self.resources = resources
        self.menu = MENU
        self.money = 0

    def run(self):
        x = input('What would you like? (espresso/latte/cappuccino): ')
        if x == 'off':
            exit(1)
        elif x == 'report':
            print(self.resources)
            print(f"Money: {self.money}")
            self.run()
        elif x in ('espresso', 'latte', 'cappuccino'):
            self.check_resources(x)
            self.process_coins(x)
            print(f"Here is your {x}. Enjoy!")
            self.run()
        else:
            print('Unrecognized command. Please try again')
            self.run()

    def check_resources(self, coffee):
        ingredients = MENU[coffee]['ingredients']
        for key, value in ingredients.items():
            available = self.resources[key]
            if value > available:
                print(f'Sorry there is not enough {key}.')
                self.run()
                # TODO Could make it calculate which coffess are available
        for key, value in ingredients.items():
            self.resources[key] -= value

    def process_coins(self, coffee):
        cost = MENU[coffee]['cost']
        money = 0
        for coin_type, value in TYPES_OF_COINS.items():
            n_coins = input(f"How many {coin_type}?: ")
            money += float(n_coins) * value
        if money < cost:
            "Sorry that's not enough money. Money refunded."
            self.run()
        else:
            self.money += cost
            print(f"Here is ${round(money - cost, 2)} in change.")


if __name__ == '__main__':
    cm = coffee_machine()
    cm.run()

