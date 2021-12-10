# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combinedName = name1 + name2
combinedNameLowerCase = combinedName.lower()

findT = combinedNameLowerCase.count("t")
findR = combinedNameLowerCase.count("r")
findU = combinedNameLowerCase.count("u")
findE = combinedNameLowerCase.count("e")

trueValue = findT + findR + findU + findE

findL = combinedNameLowerCase.count("l")
findO = combinedNameLowerCase.count("o")
findV = combinedNameLowerCase.count("v")
findE = combinedNameLowerCase.count("e")

loveValue = findL + findO + findV + findE

totalValue = str(trueValue) + str(loveValue)
loveScore = int(totalValue)

if (loveScore < 10) or (loveScore > 90):
    print(f"Your score is: {loveScore}, you go like together coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"Your score is: {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}")
