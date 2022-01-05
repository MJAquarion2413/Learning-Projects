from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    coffee_maker = CoffeeMaker()
    money_mach = MoneyMachine()
    menu = Menu()
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino/):").casefold().strip()
        if choice == "report":
            coffee_maker.report()
            money_mach.report()
        elif choice == "off":
            break
        else:
            item = menu.find_drink(choice)
            if item is None:
                continue
            check = coffee_maker.is_resource_sufficient(item)
            if check is False:
                continue
            money_check = money_mach.make_payment(item.cost)
            if money_check is False:
                continue
            coffee_maker.make_coffee(item)


if __name__ == "__main__":
    main()

###Options to add for fun:
# - refilling the machine
# - changing costs, resources needed
# - adding recipes
# -
