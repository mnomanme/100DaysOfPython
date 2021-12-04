#Data Types

# Sting

print("Hello"[4])
print("121" + "23434")

#Integer

print(123 + 445)

#Float

3.141519

#Boolean

True
False

# Type Error, Type Conversion, Type Checking

# numChar = len(input("What is your name?"))
# newNumchar = str(numChar)

# print("Your name has " + newNumchar + " characters.")

# print(type(numChar))

a = float(121)
print(type(a))

print(70 + float("100.40"))
print(str(100) + str(44))

# Mathematical Operations

3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

# PEMDASLR
# Parenthesis ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

print(3 * 3 + 3 / 3 - 3)

# Number Manipulation and F Strings

print(int(7 / 3))
print(round(7 / 3, 2))
print (type(8 // 3) ) #floor Division

result = 4 / 2
result /= 2

print(result)

score = 0


#User scores a point
# score = score + 1
score += 1

print(score)

score = 0
height = 1.8
isWining = True

print(f"your score is {score}, your height is {height},  you are wining is {isWining}")