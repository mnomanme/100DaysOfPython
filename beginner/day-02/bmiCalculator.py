# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
personHeight = float(height)
personWeight = int(weight)

bmiCalculate = personWeight / personHeight ** 2
calculateResult = int(bmiCalculate)

print(calculateResult)
