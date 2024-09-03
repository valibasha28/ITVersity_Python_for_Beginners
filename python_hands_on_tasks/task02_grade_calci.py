marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
marks4 = float(input("Enter marks for subject 4: "))
marks5 = float(input("Enter marks for subject 5: "))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
average_marks = total_marks / 5

if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
elif average_marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'Total marks are: {total_marks}')
print(f'Average marks are: {average_marks}')

print(f'The GRADE is: {grade}')