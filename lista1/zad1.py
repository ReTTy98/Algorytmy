from random import randint
import numpy as np
from statistics import mean


def create_array():  # TODO WYKONANE
    num_of_students = randint(4, 8)
    num_of_subjects = randint(4, 8)
    possible_grades = np.linspace(2.0, 5.5, 8)
    grades_students_array = np.random.choice(
        possible_grades, (num_of_students, num_of_subjects)
    )
    return grades_students_array


def failed(array):  # TODO WYKONANE
    n = randint(1, 3)
    print(f'1.Studenci z n:{n} nie zdanych przedmiotw:')
    array_failed = np.where(array < 3.0, 1, 0)
    array_failed = np.sum(array_failed, axis=1)
    print(f"{np.argwhere(array_failed >= n).flatten()}\n")



def average(array):  # TODO Optymalizacja
    students_average = np.around(np.average(array, axis=1), 2)
    print(f'2.Średnie wszystkich studentow:\n {students_average}\n')
    fake_student = np.argwhere(students_average >= 4.0).flatten()
    print(f'Lista studentow ze srednimi nie nizszymi niz 4.0:\n{fake_student}\n')

    max_average = np.argwhere(
        students_average == np.amax(students_average)).flatten()
    min_average = np.argwhere(
        students_average == np.amin(students_average)).flatten()

    print(f"""Indexy studentow o najmniejszej i najwiekszej sredniej:
max: {max_average}
min: {min_average}\n""")
    print(f"""Oceny uczniow z max i min srednia:
max:
{array[max_average, :]}
min:
{array[min_average, :]}""")


def get_highest_grades(array):
    students = np.zeros(np.shape(array)[0])
    for subject_grades in array.T:
        best_students = np.argwhere(
            subject_grades == np.amax(subject_grades)
        ).flatten()
        np.add.at(students, best_students, 1)
    final_best_students = np.argwhere(students == np.amax(students)).flatten()
    return final_best_students


if __name__ == "__main__":
    data = create_array()
    print(f"""Wygenerowana macierz:
{data}\n""")
    failed(data)
    average(data)
