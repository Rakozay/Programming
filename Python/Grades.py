# Official grades in Denmark
grades = [-3, 0, 2, 4, 7, 10, 12]
my_grades = []

enter_grades = "Enter your grades:"
print(enter_grades)

# Ask the user to enter their grades
# and then stores four grades in my_grades
for i in range(0, 4):
    entered_grades_storage = int(input())
    my_grades.append(entered_grades_storage)

# Checking purpose
print(my_grades)

for my_grade in my_grades:
    pass
if my_grade in grades:
    print("Calculated average of your grades: " + str((sum(my_grades) / len(my_grades))))
else:
    print("You entered a grade that is not known.")



