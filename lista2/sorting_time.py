import random
import timeit
from statistics import mean


def bubble_sort(L):
    bubble = L.copy()
    for i in range(len(bubble)):
        for j in range(0, (len(L) - 1) - i):
            if bubble[j] > bubble[j + 1]:
                temp = bubble[j]
                bubble[j] = bubble[j + 1]
                bubble[j + 1] = temp
    return bubble


def insertion_sort(L):
    insertion = L.copy()
    for i in range(len(insertion)):
        for j in range(0, i):
            if insertion[i] < insertion[j]:
                temp = insertion[i]
                insertion[i] = insertion[j]
                insertion[j] = temp
    return insertion


def selection_sort(L):
    selection = L.copy()
    for i in range(len(selection)):
        for j in range(i + 1, len(selection)):
            if selection[i] > selection[j]:
                temp = selection[i]
                selection[i] = selection[j]
                selection[j] = temp
    return selection


if __name__ == '__main__':
    n = 10
    list = random.choices(range(100), k=n)

    time_bubble = timeit.repeat('bubble_sort(list)', 'from __main__ import bubble_sort,list', repeat=10, number=1)
    time_insertion = timeit.repeat('insertion_sort(list)', 'from __main__ import insertion_sort,list', repeat=10,
                                   number=1)
    time_selection = timeit.repeat('selection_sort(list)', 'from __main__ import selection_sort,list', repeat=10,
                                   number=1)
    print(f"""
MAXY/ŚREDNIE:
Bubble:
{max(time_bubble)} / {mean(time_bubble)}
Insertion:
{max(time_insertion)} / {mean(time_insertion)}
Selection
{max(time_selection)} / {mean(time_selection)}""")


