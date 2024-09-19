#Basic Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the seconnd number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
else: 
    result = num1 / num2

print(f"{num1} {operation} {num2} = {result}")

