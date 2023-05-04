from menu import MENU, resources


def check_resource(drink):
    refill = 0
    milk_needed = MENU[drink]["ingredients"]["milk"]
    water_needed = MENU[drink]["ingredients"]["water"]
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    milk_have = resources["milk"]
    water_have = resources["water"]
    coffee_have = resources["coffee"]

    if milk_have < milk_needed:
        print("milk is not enough")
        print("Ask the staff to refill")
        print()
        refill = 1

    if water_have < water_needed:
        print("water is not enough")
        print("Ask the staff to refill")
        print()
        refill = 1

    if coffee_have < coffee_needed:
        print("coffee is not enough")
        print("Ask the staff to refill")
        print()
        refill = 1
    return refill


def ask_money():
    dollar_input = int(input("how many dollar you insert"))
    cent_input = int(input("how many cent you insert"))
    return dollar_input, cent_input


def check_money(total_user_money, drink):
    refund = 0
    drink_cost = MENU[drink]["cost"]
    if total_user_money < drink_cost:
        print("“Sorry that's not enough money. Money refunded.”")
        refund = 1
        return refund
    print(f"The cost of the {drink} is {drink_cost}")
    print(f"you have inserted {total_user_money}")
    return_money = total_user_money - drink_cost
    print(f"You get {return_money} in return")
    return refund


def transaction(drink):
    milk_needed = MENU[drink]["ingredients"]["milk"]
    water_needed = MENU[drink]["ingredients"]["water"]
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    milk_have = resources["milk"]
    water_have = resources["water"]
    coffee_have = resources["coffee"]
    resources["milk"] = milk_have - milk_needed
    resources["water"] = water_have - water_needed
    resources["coffee"] = coffee_have - coffee_needed
    print(f"Here is your {drink}. Enjoy!")


money_in_machine = 0
status = "on"
while status == "on":
    print()
    user_input = input("What would you like? (espresso/latte/cappuccino:)")
    if user_input == "report":
        print(resources)
        print(f"The machine has € {money_in_machine} ")

    if user_input == "off":
        print("turning off the machine")
        status = "off"

    if user_input == "espresso":

        check_refill = check_resource("espresso")
        if check_refill == 0:
            dollar_input, cent_input = ask_money()
            total_user_money = dollar_input + (cent_input / 100)
            refund = check_money(total_user_money, "espresso")
            if refund == 0:
                transaction("espresso")
                money_in_machine += MENU["espresso"]["cost"]

    if user_input == "latte":

        check_refill = check_resource("latte")
        if check_refill == 0:
            dollar_input, cent_input = ask_money()
            total_user_money = dollar_input + (cent_input / 100)
            refund = check_money(total_user_money, "latte")
            if refund == 0:
                transaction("latte")
                money_in_machine += MENU["latte"]["cost"]

    if user_input == "cappuccino":
        check_refill = check_resource("cappuccino")
        if check_refill == 0:
            dollar_input, cent_input = ask_money()
            total_user_money = dollar_input + (cent_input / 100)
            refund = check_money(total_user_money, "cappuccino")
            if refund == 0:
                transaction("cappuccino")
                money_in_machine += MENU["cappuccino"]["cost"]
