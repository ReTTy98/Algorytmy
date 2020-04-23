import algorytmy
import matplotlib.pyplot as mat  

checks = [10,20,50,100,200,500,1000]

bubble_times_avg = []
insertion_times_avg = []
selection_times_avg = []
bubble_times_max = []
insertion_times_max = []
selection_times_max = []

for check in checks:
    
    temp_bubble_times = []
    temp_insertion_times = []
    temp_selection_times = []

    for i in range(10):

        bubble_list , bubble_time = algorytmy.bubble_sort(algorytmy.random_list_generator(check))
        insertion_list, insertion_time = algorytmy.insertion_sort(algorytmy.random_list_generator(check))
        selection_list, selection_time = algorytmy.selection_sort(algorytmy.random_list_generator(check))

        temp_bubble_times.append(bubble_time)
        temp_insertion_times.append(insertion_time)
        temp_selection_times.append(selection_time)

    bubble_times_max.append(max(temp_bubble_times))
    insertion_times_max.append(max(temp_insertion_times))
    selection_times_max.append(max(temp_selection_times))

    bubble_times_avg.append(sum(temp_bubble_times) / len(temp_bubble_times))
    insertion_times_avg.append(sum(temp_insertion_times) / len(temp_insertion_times))
    selection_times_avg.append(sum(temp_selection_times) / len(temp_selection_times))


fig, ax = mat.subplots()
ax.plot(bubble_times_avg, checks, 'r--', label= "[Średnia] Bubble")
ax.plot(insertion_times_avg, checks, 'g--', label='[Średnia] Insertion')
ax.plot(selection_times_avg, checks, 'b--', label='[Średnia] Selection')
ax.plot(bubble_times_max, checks, 'r', label='[Max] Bubble')
ax.plot(insertion_times_max, checks, 'g', label='[Max] Insertion')
ax.plot(selection_times_max, checks, 'b', label='[Max] Selection')
mat.title('Czas działania wybranych algorytmów sortujących')
mat.xlabel('Czas w sekundach [s]')
mat.ylabel('Długości ciągów [n]')
mat.legend(loc='lower right')
mat.show()