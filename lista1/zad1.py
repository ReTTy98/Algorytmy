from random import choices, randint
import numpy as np
from statistics import mean


def create_array(students, subjects):
    grades = np.linspace(2.0, 5.5, 8)
    array = []
    while students > 0:
        array.append(choices(grades, k=subjects))
        students -= 1
    array = np.array(array)
    return array


def failed(array, n):
    failed_students = 0
    for row in array:
        failed_subjects = 0
        for grade in row:
            if grade < 3.0:
                failed_subjects += 1
        if failed_subjects >= n:
            failed_students += 1
    return failed_students


def average(array):
    grades = []
    for row in array:
        grades.append(mean(row))
    print(grades)
    max_average = max(grades)
    min_average = min(grades)
    grades = np.array(grades)
    max_index = np.argwhere(grades == max_average)
    min_index = np.argwhere(grades == min_average)
    max_list = []
    min_list = []
    for i in max_index:
        max_list.append(array[i])
    for i in min_index:
        min_list.append(array[i])
    max_list = np.array(max_list)
    min_list = np.array(min_list)
    print(max_list)
    print(min_list)
    return max_list , min_list


def column_grades(array):
    array_t = array.T
    array_i = np.shape(array_t)[0]
    print(array_i)
    print(array_t)
    max_value = []
    for i in array_t:
        max_value.append(max(i))
    print(max_value)
    pass


if __name__ == "__main__":
    np.set_printoptions(precision=2)
    data = create_array(randint(3, 5), randint(3, 5))
    print(data)
    print(failed(data, randint(1, 3)))
    average_data = average(data)
    print("============================")
   # column_grades(data)