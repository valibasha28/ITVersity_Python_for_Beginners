def greet(fname, lname):
    print(f"Hello, {fname} {lname}!!!\n")

def multiply(num1, num2):
    result = num1 * num2
    print(f"Multiplication of {num1} and {num2} is: {result}\n") 

def is_adult(age):
    if age>18:
        print("Person is Adult")
    else:
        print("Person is Not an Adult")

print("Please enter your First Name and Last Name")
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
greet(fname, lname)

print("Multiplication operation using functions")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
multiply(num1, num2)

print("Person is Adult or not")
age = int(input("Enter the age to check adult or not: "))
is_adult(age)
