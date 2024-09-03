def greet(name):
    print(f"Hello, {name}!! Welcome to ITVersity..!\n\n")

def add(num1, num2):
    print("Sum is: ",(num1+num2))
    print('\n\n')

def is_even(number):
    if number % 2 == 0:
        print(f"{number} is EVEN!")
    else:
        print(f"{number} is ODD")

greet('Basha')

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
add(num1, num2)

number = int(input("Enter the number to even or odd: "))
is_even(number)
