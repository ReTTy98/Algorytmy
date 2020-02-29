import numpy as np
from random import randint, choices


class HighestGrade:
    def __init__(self, data_array):
        self.data_array = data_array
        self.array = np.copy(data_array)

    def array_print(self):
        print(self.array)

    def best_grade_of_subject(self):
        array = self.array.T
        array_iterator = np.shape(array)[0]
        array_iterator = np.arange(array_iterator)
        best_grade_index = []

        for i in array_iterator:
            max_grade = max(array[i])
            best_grade_index.append(np.nonzero(array[i] == max_grade))

        best_grade_index = np.array(best_grade_index).flatten()
        students = []
        return best_grade_index


def create_array(students, subjects):
    grades = np.linspace(2.0, 5.5, 8)
    array = []
    while students > 0:
        array.append(choices(grades, k=subjects))
        students -= 1
    array = np.array(array)
    return array


if __name__ == "__main__":
    data = HighestGrade(create_array(randint(4, 7), randint(4, 7)))
    data.array_print()
    print(data.best_grade_of_subject())