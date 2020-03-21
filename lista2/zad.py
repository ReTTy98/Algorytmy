import matplotlib.pyplot as plt
from sorting_time import bubble_sort, selection_sort, insertion_sort
import random
import timeit
from statistics import mean

if __name__ == '__main__':
    n_elements = [10, 20, 50, 100, 200, 500, 1000]
    elements 
    bubble_chart_max = []
    selection_chart_max = []
    insertion_chart_max = []
    bubble_chart_average = []
    selection_chart_average = []
    insertion_chart_average = []
    for i in n_elements:
        bubble_time = timeit.repeat('bubble_sort(elements)',
                                    'from __main__ import bubble_sort,elements',
                                    repeat=10,
                                    number=1)
        selection_time = timeit.repeat('selection_sort(elements)',
                                       'from __main__ import selection_sort,elements',
                                       repeat=10,
                                       number=1)
        insertion_time = timeit.repeat('insertion_sort(elements)',
                                       'from __main__ import insertion_sort,elements',
                                       repeat=10,
                                       number=1)

        bubble_chart_max.append(max(bubble_time))
        selection_chart_max.append(max(selection_time))
        insertion_chart_max.append(max(insertion_time))
        bubble_chart_average.append(mean(bubble_time))
        selection_chart_average.append(mean(selection_time))
        insertion_chart_average.append(mean(insertion_time))
        n = i
    print(f"""
{bubble_chart_max}
{bubble_chart_average}
{selection_chart_max}
{selection_chart_average}
{insertion_chart_max}
{insertion_chart_average}""")

