import numpy as np
from random import randint


def s_d():

    x = np.random.choice(
        np.arange(0, 100), (randint(4, 6),randint(4, 6))
    )
    y = np.random.choice(
        np.arange(0, 100), (np.shape(x)[0], np.shape(x)[1])
    )
    symmetric_difference = np.sum(np.absolute(x - y))

    print(f'''Pierwsza macierz:
{x}

Druga Macierz:
{y}

Różnica symetryczna: {symmetric_difference}''')




if __name__ == '__main__':
    s_d()


