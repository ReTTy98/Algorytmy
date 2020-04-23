from singly_linked_list import SinglyLinkedList
from the_office import Client, Office, Worker

import simulation

office = Office()
queue = SinglyLinkedList()

# ma być: 3xA, 3xB, 3xC, 1xE


for i in range(3):
    office.add_worker(Worker('A'))
    office.add_worker(Worker('B'))
    office.add_worker(Worker('C')) 

office.add_worker(Worker('E')) 

for i in range(30):
    c = Client()
    print(c, 'lines up')
    queue.add(c)


simulation.run_simulation(office, queue)

office.print_summary()

'''
# Propozycja usprawnienia:

Wykorzystanie stringów określających typ pracownika
i porównywanie tych stringów z typem zadania nie jest
wydajne, porównania łańcuchów znaków są z natury powolne,
nawet jesli mówimy o łańcuchach jednoznakowych

Szybszą metodą byłoby wykorzystanie zestawu flag bitowych
określających typ zadania: na przykład

```
A = 0b001
B = 0b010
C = 0b100

E = 0b111
```

Wtedy sprawdzanie czy pracownik potrafi obsłużyć dane zadanie,
wykonywane byłoby w następujacy sposób:

```
if client.task_tye & worker.specialisation != 0:
    # Przydzielić zadanie
```

Taki zestaw flag możnaby zaimplementować za pomocą zwykłych
intów w Pythonie, lub za pomocą biblioteki struct (co pozwalałoby
na lepsze możliwości rozbudowy i utrzymywalności kodu)
'''