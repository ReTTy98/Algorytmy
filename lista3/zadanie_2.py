import matplotlib.pyplot as plt

import simulation
from singly_linked_list import SinglyLinkedList
from the_office import Client, Office, Worker

# Część 1sza
# Uruchomić tą samą 30klientową kolejkę na 2 różnych biurach

office_1 = Office()
office_2 = Office()

for i in range(3):
    office_1.add_worker(Worker('A'))
    office_1.add_worker(Worker('B'))
    office_1.add_worker(Worker('C'))

for i in range(2):
    office_2.add_worker(Worker('A'))
    office_2.add_worker(Worker('B'))
    office_2.add_worker(Worker('C'))
    office_2.add_worker(Worker('E'))


queue_1 = SinglyLinkedList()
queue_2 = SinglyLinkedList()

for i in range(30):
    queue_1.add(Client())
    queue_2.add(Client())


simulation.run_simulation(office_1, queue_1)
simulation.run_simulation(office_2, queue_2)


office_1.print_summary()
office_2.print_summary()

del office_1
del office_2
del queue_1
del queue_2

# Część 2ga
# Narysować histogram dla 100 kolejek

office_1_times = []
office_2_times = []

for i in range(100):

    office_1 = Office()
    office_2 = Office()

    for i in range(3):
        office_1.add_worker(Worker('A'))
        office_1.add_worker(Worker('B'))
        office_1.add_worker(Worker('C'))

    for i in range(2):
        office_2.add_worker(Worker('A'))
        office_2.add_worker(Worker('B'))
        office_2.add_worker(Worker('C'))
        office_2.add_worker(Worker('E'))


    queue_1 = SinglyLinkedList()
    queue_2 = SinglyLinkedList()

    for i in range(30):
        queue_1.add(Client())
        queue_2.add(Client())


    simulation.run_simulation(office_1, queue_1)
    simulation.run_simulation(office_2, queue_2)

    office_1_times.append(office_1.worked_time)
    office_2_times.append(office_2.worked_time)


office_1_avg = sum(office_1_times)/len(office_1_times)
office_2_avg = sum(office_2_times)/len(office_2_times)

print(f"""
Średni czas pracy:
9 okienkowy urząd: {office_1_avg}
8 okienkowy urząd: {office_2_avg}""")

fig, ax = plt.subplots()


plt.hist(office_1_times, color='r', label='9 okienek')
plt.hist(office_2_times, color='g', label='8 okienek')
plt.xlabel('Ilość iteracji')
plt.ylabel('Długość iteracji')
plt.legend(loc='lower right')

plt.text(1, 1, f"""
Średni czas pracy:
9 okienkowy urząd: {office_1_avg}
8 okienkowy urząd: {office_2_avg}""")


plt.show()

'''

# Omówienie wyników:

Obie konfiguracje biur uzyskują zbliżone czasy
łącznej obsługi klientów, mimo różnej liczby
pracowników - wynika to z faktu, że biura posiadające
pracowników klasy 'E' są bardziej elastyczne
i nie pozwalają na tworzenie się w kolejkach 'korków',
czyli sytuacji, gdy pierwsza osoba w kolejce czeka,
ponieważ nikt z wolnych pracowników nie jest
kompatybilny z jej zadaniem.

# Propozycja usprawnienia:

Kolejka powinna zostać rozbita na trzy,
osobne dla każdego zadania. W ten sposób
nie dojdzie do sytuacji, gdy klient
będzie blokował kolejkę swoim zadaniem,
podczas gdy pracownicy obsługujący inne
zadania będą czekali bezczynnie.
'''