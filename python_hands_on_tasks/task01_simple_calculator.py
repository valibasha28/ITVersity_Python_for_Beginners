num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose an operation (+, - , *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error, division by zero"
else:
    result = "Invalid operation!! Try again!"

print(f"Result: {result}")
