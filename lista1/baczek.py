import numpy as np
import random

num_of_students = random.randrange(3, 4)
num_of_subjects = random.randrange(3, 4)

possible_grades = [i / 2 for i in range(4, 12)]

# Wiersz to student
# Kolumna to przedmiot

grades_students_array = np.random.choice(
    possible_grades, (num_of_students, num_of_subjects)
)

print(grades_students_array)
print()
students = np.zeros(num_of_students)
print(students)

for subject_grades in grades_students_array.T:
    best_students = np.argwhere(
        subject_grades == np.amax(subject_grades)
    ).flatten()
    print("XD")
    print(best_students)
    np.add.at(students, best_students, 1)

print(students)

print()

print(np.argwhere(students == np.amax(students)).flatten())