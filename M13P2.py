# Kirill M13P2 11/05/2026

# List of names and 3 rows of grades
student_name = ['Bob', 'Josh', 'Chris', 'Alex', 'Peter', 'Tom', 'Sam', 'Joshua', 'Jacob', 'Ricky']
grades = [75, 81, 92, 40, 31, 94, 10, 41, 56, 72,
          42, 17, 89, 3, 65, 28, 94, 51, 12, 76,
          18, 93, 41, 7, 62, 85, 30, 54, 99, 23]

# Creating a dictionary with a list for each stundent with 3 grades
student_dict = {}
# Creating a loop for specific indext and it grade
for i in range(len(student_name)):
    student_dict[student_name[i]] = grades[i*3 : (i+1) * 3]

# Define function
def average_student(data):
# Creating empty list
    average_list = []
    for name, grade_list in data.items():
# Finding mean value for each student
        avg = sum(grade_list) / len(grade_list)
        average_list.append([name, round(avg, 2)])
    return average_list

# Prining students grade average for each stundent
print()
print("Students grade average")
# Using function for showing stundet grade average
student_avg = average_student(student_dict)
for student in student_avg:
    print(f"{student[0]:<10} | Average {student[1]}")

# Prining class average for 3 rows
print()
print("Class average by test")
# Define range to use text index
for test_index in range(3):
    test_scores = []
    for scores in student_dict.values():
        test_scores.append(scores[test_index])
# Finding average for test
    test_avr = sum(test_scores) / len(test_scores)
    print(f"Test {test_index + 1} Average | {test_avr:.2f}")
