print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n ")
add_pepperoni = input("Do you want pepperoni? Y or N\n ")
extra_cheese = input("Do you want extra cheese? Y or N\n ")


pepperoni = 0
extraCheese = 0

if size.upper() == "S":
    price = 15
    if add_pepperoni.upper() == "Y":
        pepperoni = 2
    if extra_cheese.upper() == "Y":
        extraCheese = 1
elif size.upper() == "M":
    price = 20
    if add_pepperoni.upper() == "Y":
        pepperoni = 3
    if extra_cheese.upper() == "Y":
        extraCheese = 1
elif size.upper() == "L":
    price = 25
    if add_pepperoni.upper() == "Y":
        pepperoni = 3
    if extra_cheese.upper() == "Y":
        extraCheese = 1

bill = price + pepperoni + extraCheese
print (f"Your final bill for the {size.upper()} pizza is ${bill}, enjoy your pizza and please come again")
