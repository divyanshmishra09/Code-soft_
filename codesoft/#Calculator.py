#Calculator
print("Choose Operation")
print("1. Addtion")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")
#Take user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choose = int(input("choose operation 1, 2, 3, 4: "))
if choose == 1:
    print(num1, "+", num2, "=", num1+num2)
elif choose == 2:
    print(num1, "-", num2, "=", num1-num2)
elif choose == 3:
    print(num1, "*", num2, "=", num1*num2)
elif choose == 4:
    print(num1, "/", num2, "=", num1/num2)
else:
    print("Invalid")

