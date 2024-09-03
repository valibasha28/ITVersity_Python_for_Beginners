import utilities

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

addition = utilities.add(a,b)
subtraction = utilities.sub(a,b)

print(f"Sum of {a} and {b} is: {addition}")
print(f"Difference of {a} and {b} is: {subtraction}")