password = input("Enter a password: ")

length = len(password)>=8
upper = any(char.isupper() for char in password)
lower = any(char.islower() for char in password)
digit = any(char.isdigit() for char in password)
special = any(char in "!@#$%^&*()_+" for char in password)

if length and upper and lower and digit and special:
    print("Password is Strong!")
else:
    print("Password is Weak..")