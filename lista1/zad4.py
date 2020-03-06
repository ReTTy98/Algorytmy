import numpy as np
import string
import random


def create_bill():
    bill = np.empty(random.randint(6, 8), )


def available_products():
    products_array = np.zeros((random.randint(4, 9), 3), dtype=float)
    row_quantity = np.shape(products_array)[0]
    print(products_array)
    print(row_quantity)
    products_array[:, 0] = product_code_generate(row_quantity)
    print(products_array)
    products_array[:, 1] = prices_generate(row_quantity)
    products_array[:,2] = product_type_generate(row_quantity)
    print(products_array)


def testing_bill():
    pass


def product_code_generate(how_many, size=4, chars=string.digits):
    products_codes = []
    for i in range(how_many):
        x = ''.join(random.choice(chars) for i in range(size))
        x = int(x)
        products_codes.append(x)
        # products_codes.append(''.join(random.choice(chars) for i in range(size)))
    return products_codes


def prices_generate(how_many):
    prices = []
    for i in range(how_many):
        x = round(random.uniform(1, 30),2)
        prices.append(x)
    print(f"GOTOWKA:{prices}")
    return prices

def product_type_generate(how_many):
    product_type = []
    for i in range(how_many):
        x = random.randint(0,1)
        product_type.append(x)
    return product_type

if __name__ == "__main__":
    available_products()

"""
Paragon = [Nr.Klenta , numer towary , szt/kg  ]
Dostepne produkty = [numer towaru, cene-szt/kg , szt/wg?]




"""
