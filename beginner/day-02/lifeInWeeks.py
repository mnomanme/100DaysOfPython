# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
inPersonAge = int(age)
inPersonDays = inPersonAge * 365
inPersonWeeks = inPersonAge * 52
inPersonMonths = inPersonAge * 12

totalDaysLeft = 90 * 365 - inPersonDays
totalWeeksLeft = 90 * 52 - inPersonWeeks
totalMonthsLeft = 90 * 12 - inPersonMonths

print(f"You have {totalDaysLeft} days, {totalWeeksLeft} weeks, and {totalMonthsLeft} months left.")

