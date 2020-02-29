from random import randint
import numpy as np
from statistics import mean


def failed(array):  # TODO Optymalizacja
    n = randint(1,3)
    print(f'Studenci z n:{n} nie zdanych przedmiotw:')
    array_failed = np.where(array < 3.0, 1, 0)
    array_failed = np.sum(array_failed, axis=1)
    print(np.argwhere(array_failed >= n).flatten())
    return array_failed


def create_array():
    num_of_students = randint(4, 8)
    num_of_subjects = randint(4, 8)
    possible_grades = np.linspace(2.0, 5.5, 8)
    grades_students_array = np.random.choice(
        possible_grades, (num_of_students, num_of_subjects)
    )
    return grades_students_array


data = create_array()
failed(data)
