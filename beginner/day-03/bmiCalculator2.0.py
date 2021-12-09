# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmiCalculate = weight / (height ** 2)
calculateResult = round(float(bmiCalculate))

# print(calculateResult)

if calculateResult < 18.5:
    print(f"Your BMI is {calculateResult}, you are underweight.")
elif calculateResult < 25:
    print(f"Your BMI is {calculateResult}, you have a normal weight.")
elif calculateResult < 30:
    print(f"Your BMI is {calculateResult}, you are slightly overweight")
elif calculateResult < 35:
    print(f"Your BMI is {calculateResult}, you are obese.")
else:
    print(f"Your BMI is {calculateResult}, you are clinically obese.")
