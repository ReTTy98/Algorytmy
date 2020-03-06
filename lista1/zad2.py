import numpy as np
from random import randint


def s_d():
    x = np.random.choice(
        np.arange(0, 100), (randint(4, 6),randint(4, 6))
    )
    y = np.random.choice(
        np.arange(0, 100), (np.shape(x)[0], np.shape(x)[1])
    )
    symmetric_difference = np.absolute(x - y)

    print(f"""Macierz x:
{x}

Macierz y:
{y}

x-y:
{x-y}

Odległość symetryczna:
{symmetric_difference}
    """)


s_d()
