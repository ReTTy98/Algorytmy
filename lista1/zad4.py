import numpy as np
import string
import random

def create_bill():
    pass


def available_products():



def product_code_generate(how_many, size=6, chars=string.ascii_uppercase + string.digits):
    products_codes = []
    for i in range(how_many):
        products_codes.append(''.join(random.choice(chars) for i in range(size)))
    return products_codes


if __name__ == "__main__":
    print(product_code_generate(4))




"""
[numer produktu , nazwa produktu, Czy w kg? , cena za szt/kg , ilosc]




"""