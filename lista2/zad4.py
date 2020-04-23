import time
from algorytmy import random_list_generator, bubble_sort



def bubble_sort_but_better(L):
    bubble = L.copy()
    start = time.time()
    for i in range(len(bubble)):
        old_bubble = bubble.copy()
        for j in range(0, (len(bubble) - 1) - i):
            if bubble[j] > bubble[j + 1]:
                temp = bubble[j]
                bubble[j] = bubble[j + 1]
                bubble[j + 1] = temp
        if old_bubble == bubble:
            break
    return bubble, time.time() - start


def bubble_sort_but_worse(L):
    bubble = L.copy()
    start = time.time()
    for i in range(len(bubble)):
        for j in range(0, len(bubble) - 1):
            if bubble[j] > bubble[j + 1]:
                temp = bubble[j]
                bubble[j] = bubble[j + 1]
                bubble[j + 1] = temp
    return bubble, time.time() - start


if __name__ == "__main__":
    unsorted_list = random_list_generator(1000)
    sorted_list = sorted(unsorted_list)

    #Porownuje zmodyfikowany algorytm z oryginalnym 
    print(bubble_sort_but_better(sorted_list)[1])   
    print(bubble_sort(sorted_list)[1])

    print()

    #Znowu to robie
    print(bubble_sort_but_worse(unsorted_list)[1])
    print(bubble_sort(unsorted_list)[1])