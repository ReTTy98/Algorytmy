import numpy as np
from random import randint, choices


def get_highest_grades(array):
    students = np.zeros(np.shape(array)[0])
    for subject_grades in array.T:
        best_students = np.argwhere(
            subject_grades == np.amax(subject_grades)
        ).flatten()
        np.add.at(students, best_students, 1)
    final_best_students = np.argwhere(students == np.amax(students)).flatten()
    return  final_best_students

def create_array(students, subjects):
    grades = np.linspace(2.0, 5.5, 8)
    array = []
    while students > 0:
        array.append(choices(grades, k=subjects))
        students -= 1
    array = np.array(array)
    return array


if __name__ == "__main__":
    data = create_array(randint(4, 5), randint(4, 5))
    print(data)
    print()
    print(get_highest_grades(data))
