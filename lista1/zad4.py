import numpy as np
import random


def create_bill_array(products_list):
    products = products_list[:, 0]
    type_of_product = products_list[:, 2]

    # Stworz macierz zawierajaca numery klientow
    how_many_clients = random.randint(7, 12)
    clients_numbers = random.sample(range(30), k=how_many_clients)
    clients_array = np.array(clients_numbers).reshape(how_many_clients, 1)

    # Stworz macierz kupionych produktow
    bought_products = random.choices(products, k=how_many_clients)
    bought_products_array = np.array(bought_products).reshape(how_many_clients, 1)

    # Stworz slownik zawierajacy informacje o typie produktu
    type_check = {}
    for i in range(len(products)):
        type_check[products[i]] = type_of_product[i]

    # Stworz macierz wagi lub sztuk kupionych produktow
    products_quantity = []
    for product in bought_products:
        if type_check[product] == 0:
            products_quantity.append(random.randint(1, 20))
        elif type_check[product] == 1:
            products_quantity.append(round(random.uniform(1, 30), 2))
        else:
            print("HALO COŚ TUTAJ JEST NIE TAK")
    products_quantity_array = np.array(products_quantity).reshape(how_many_clients, 1)

    # Stworz macierz rachunku
    bill_array = np.concatenate((clients_array, bought_products_array, products_quantity_array), axis=1)

    return bill_array


def prices_generate(quantity):
    generated_prices = []
    for i in range(quantity):
        x = round(random.uniform(1, 30), 2)
        generated_prices.append(x)
    generated_prices = np.array(generated_prices).reshape(quantity, 1)
    return generated_prices


def product_code_generate(quantity):
    generated_codes = []
    for i in range(quantity):
        x = random.randint(1000, 9999)
        generated_codes.append(x)
    generated_codes = np.array(generated_codes).reshape(quantity, 1)
    return generated_codes


def product_list_generate(prices, codes, quanity):
    # 0 - Na sztuki   |||  1 - Na wage
    type_of_product = np.array(random.choices(range(2), k=quanity)).reshape(quanity, 1)
    generated_product_list = np.concatenate((codes, prices, type_of_product), axis=1)
    return generated_product_list


def money_spent(bill, products):
    clients_codes = bill[:, 0]
    clients_codes = clients_codes.reshape(np.shape(clients_codes)[0], 1)
    bought_product_codes = bill[:, 1]
    quantity_bought = bill[:, 2]
    product_codes = products[:, 0]
    product_prices = products[:, 1]

    price_list = {}
    for i in range(len(product_codes)):
        price_list[product_codes[i]] = product_prices[i]

    spent_money_per_client = []
    n = 0
    for product in bought_product_codes:
        total = round((price_list[product] * quantity_bought[n]), 2)
        spent_money_per_client.append(total)
        n = + 1
    spent_money_per_client = np.array(spent_money_per_client).reshape(len(spent_money_per_client), 1)

    money_spent_array = np.concatenate((clients_codes, spent_money_per_client), axis=1)
    return money_spent_array


if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    # Tworzenie listy produktów
    how_many = random.randint(8, 10)
    prices = prices_generate(how_many)
    codes = product_code_generate(how_many)
    products_list = product_list_generate(prices, codes, how_many)

    # Tworzenie paragonów
    bill = create_bill_array(products_list)

    # Obliczanie wydatkow na klienta
    expenses = money_spent(bill, products_list)

    print(f"""
PIERWSZA MACIERZ LISTY PRODUKTOW DOSTEPNYCH W SKLEPIE
======================================
NUMER_PRODUKTU | CENA ZA SZT/KG | 0-NA SZTUKI , 1-NA WAGE
{products_list}
=======================================
DRUGA MACIERZ PARAGONOW
=======================================
NUMER KLIENTA | NUMER TOWARU | ZAKUPIONA ILOSC
{bill}
========================================
TRZECIA MACIERZ WYDANYCH PIENIEDZY
==========================================
NUMER KLIENTA | ILOSC WYDANYCH PIENIAZKOW
{expenses}""")
