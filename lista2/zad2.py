import algorytmy
import random

unsorted_numbers = random.choices(range(20000), k=400)

bubble_times_list = []
insertion_times_list = []
selection_times_List = []

for i in range(10):
    bubble_list , bubble_time = algorytmy.bubble_sort(unsorted_numbers)
    insertion_list, insertion_time = algorytmy.insertion_sort(unsorted_numbers)
    selection_list, selection_time = algorytmy.selection_sort(unsorted_numbers)

    bubble_times_list.append(bubble_time)
    insertion_times_list.append(insertion_time)
    selection_times_List.append(selection_time)




print(f"""
Bubble -  Average:{sum(bubble_times_list) / len(bubble_times_list)}, Max:{max(bubble_times_list)}
Insertion - Average:{sum(insertion_times_list) / len(insertion_times_list)}, Max:{max(insertion_times_list)}
Selection - Average: {sum(selection_times_List)/ len(selection_times_List)}, Max: {max(selection_times_List)}""")

