from algorytmy import bubble_sort, random_list_generator
from zad4 import bubble_sort_but_better, bubble_sort_but_worse

n = random_list_generator(1000)

_ , time_one = bubble_sort(n)
_, time_two = bubble_sort_but_better(n)
_, time_three = bubble_sort_but_worse(n)


print(f"""
Oryginalny Bubble: 
{time_one}
Przerywający iteracje:
{time_two}
Naiwnie lecący do końca:
{time_three}""")
