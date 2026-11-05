# Kirill M13P1 10/27/2026

# List of names and grades
student_name = ['Bob', 'Josh', 'Chris', 'Alex', 'Peter', 'Tom', 'Sam', 'Joshua', 'Jacob', 'Ricky']
grades = [75, 81, 92, 40, 31, 94, 10, 41, 56, 72]

# Define function display
def display(name, score):
# Create dictionary with key values
    student_dict = dict(zip(name, score))
# Finding average using sum of grade list and length number of student list
    average = sum(grades) / len(student_name)
    print()
# Creating header
    print(f"{'Student name:':<15} {'Grades:':<10}")
# Using value from dictionary for printing them
    for name, score in student_dict.items():
# Print list value
        print(f"{name:<15} | {score:<10}")
    print()
# Printing average value
    print(f"Class average: {average}")

# Calling for the function
display(student_name, grades)