# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
pizzaPrice = 0

if size == "S":
    pizzaPrice += 15
elif size == "M":
    pizzaPrice += 20
elif size == "L":
    pizzaPrice += 25
if add_pepperoni == "Y":
    if size == "S":
        pizzaPrice += 2
    if size == "M":
        pizzaPrice += 3
    if size == "L":
        pizzaPrice += 3

if extra_cheese == "Y":
    if size == "S":
        pizzaPrice += 1
    if size == "M":
        pizzaPrice += 1
    if size == "L":
        pizzaPrice += 1

print(f"Your final bill is: ${pizzaPrice}.")
