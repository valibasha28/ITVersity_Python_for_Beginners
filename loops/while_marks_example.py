total_marks = 0
continue_entry = 'yes'

while continue_entry.lower() == 'yes':
    marks = float(input("Enter the student's marks for this semester: "))
    total_marks += marks
    continue_entry = input("Are there more semester: (yes/no): ")

print(f"Total marks accumulated over all semesters is: {total_marks}")