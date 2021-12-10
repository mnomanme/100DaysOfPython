# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if size == "S":
    smallPizza = 15
    # print("pizzaPrice = 15")
    if add_pepperoni == "Y":
        PepperoniForSmallPizza = smallPizza + 2
        print(f"Your final bill is: ${PepperoniForSmallPizza}.")
        if extra_cheese == "Y":
            extraChess = smallPizza + 1 + PepperoniForSmallPizza
            print(f"Your final bill is: ${extraChess}.")
    # else:
    #     print(f"Your final bill is: ${smallPizza}.")
if size == "M":
    mediumPizza = 20
    if add_pepperoni == "Y":
        PepperoniForMediumAndLargePizza = mediumPizza + 3
        print(f"Your final bill is: ${PepperoniForMediumAndLargePizza}.")
    else:
        print(f"Your final bill is: ${mediumPizza}.")

if size == "L":
    largePizza = 25
    if add_pepperoni == "Y":
        PepperoniForMediumAndLargePizza = largePizza + 3
        print(f"Your final bill is: ${PepperoniForMediumAndLargePizza}.")
    else:
        print(f"Your final bill is: ${largePizza}.")


