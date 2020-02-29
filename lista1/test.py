import numpy as np
from random import randint, choices


def highest_grades(array_students):
    array = np.copy(array_students)
    array_t = array.T
    array_iterator = np.shape(array_t)[0]
    array_iterator = np.arange(array_iterator)
    max_value = []
    for row in array_t:
        max_value.append(max(row))
    for i in array_iterator:
        array_t[i] = np.where(array_t[i] == max_value[i], 1, 0)
    array_point = array_t.T
    max_value.clear()
    array_iterator = np.shape(array_point)[0]
    array_iterator = np.arange(array_iterator)
    for i in array_iterator:
        max_value.append(np.sum(array_point[i]))
    best_students = []
    for i in max_value:
        if i == max(max_value):
            print(i)

    return best_students


def create_array(students, subjects):
    grades = np.linspace(2.0, 5.5, 8)
    array = []
    while students > 0:
        array.append(choices(grades, k=subjects))
        students -= 1
    array = np.array(array)
    return array


#
if __name__ == "__main__":
    data = create_array(randint(4, 7), randint(4, 7))
    best_grades = highest_grades(data)
    print(f"""NOWA MACIERZ
=================================
{data}
=================================
MACIERZ TRANSPONOWANA
=================================
{data.T}
================================
INDEX NAJLEPSZEGO STUDENTA
================================
{best_grades}"""
          )

