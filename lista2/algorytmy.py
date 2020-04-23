import random
import time


def random_list_generator(x):
    return random.choices(range(10000),k=x)

def bubble_sort(L):
    bubble = L.copy()
    start = time.time()
    for i in range(len(bubble)):
        for j in range(0, (len(bubble) - 1) - i):
            if bubble[j] > bubble[j + 1]:
                temp = bubble[j]
                bubble[j] = bubble[j + 1]
                bubble[j + 1] = temp
    return bubble, time.time() - start


def insertion_sort(L):
    insertion = L.copy()
    start = time.time()
    for i in range(len(insertion)):
        for j in range(0, i):
            if insertion[i] < insertion[j]:
                temp = insertion[i]
                insertion[i] = insertion[j]
                insertion[j] = temp
    return insertion, time.time() - start


def selection_sort(L):
    selection = L.copy()
    start = time.time()
    for i in range(len(selection)):
        for j in range(i + 1, len(selection)):
            if selection[i] > selection[j]:
                temp = selection[i]
                selection[i] = selection[j]
                selection[j] = temp
    return selection, time.time() - start


"""
if __name__ == '__main__':
    unsorted_numbers = random.choices(range(20000), k=9000)
    print(f
{bubble_sort(unsorted_numbers)[1]}
{insertion_sort(unsorted_numbers)[1]}
{selection_sort(unsorted_numbers)[1]})
"""