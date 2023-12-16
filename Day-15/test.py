from data import resources

money = 0
water_resource = resources["water"]
milk_resource = resources["milk"]
coffee_resource = resources["coffee"]

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    }
}


for x in MENU:
    latte_water = MENU[x]["ingredients"]["water"]
    latte_milk = MENU[x]["ingredients"]["milk"]
    latte_coffee = MENU[x]["ingredients"]["coffee"]

    if x == "latte":
        if water_resource >= latte_water and milk_resource >= latte_milk and coffee_resource >= latte_coffee:
            print("good")


res = MENU["latte"]["ingredients"]["water"]
print(res)
