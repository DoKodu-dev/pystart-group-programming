# import biblioteki wbudowane
import os
# biblioteki doinstalowane
from tabulate import tabulate
# swoje moduły
from main import produkty



class Product:
    def __init__(self, name: str, price: float, qty: int, description: str = None) -> None:
        self.name = name
        self.price = round(price, 2)
        self.qty = qty
        self.description = description

    def __str__(self) -> str:
        return f'Nazwa: {self.name} | Cena: {self.price} | Ilość na magazynie: {self.qty}'

    def __repr__(self) -> str:
        return self.name


class Basket:
    def __init__(self) -> None:
        self.basket = []  # [produkt1, produkt2]

    def __str__(self) -> str:
        return str(self.basket)

    def add_product(self, product: Product, qty: int):
        if product.qty >= qty:
            self.basket.append(product)
            product.qty -= qty

    def show_basket(self):
        if self.basket:
            basket_sum = 0
            for product in self.basket:
                print(f'{product.name} - {product.price * product.qty} zł')
                basket_sum += product.price * product.qty
            print(f'Łączna wartość zamówienia: {basket_sum:.2f}')


class Buyer:
    def __init__(self, first_name: str, last_name: str, address: str = None, phone: str = None) -> None:
        self.basket = Basket()
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone


if __name__ == '__main__':
    # TODO: zmienić na obiekt/klasę
    magazine = [
        Product('Mysz komputerowa', 49.99, 5),
        Product('Klawiatura', 99.99, 0),
        Product('Monitor', 699.99, 3),
        Product('Kamera internetowa', 700, 123),
    ]

    while True:
        os.system('clear') # cls
        title = 'SKLEP INTERNETOWY Z SPRZĘTEM KOMPUTEROWYM'
        print('+' + '-' * (len(title)+4) + '+')
        print(f'|  {title}  |')
        print('+' + '-' * (len(title)+4) + '+')
        
        # for i, product in enumerate(magazine, start=1):
        #     if product.qty < 1:
        #         continue
        #     print(f'{i} - {product.name} ({product.price} zł)')
        to_table = [['Nazwa', 'Cena', 'Stan magazynowy'],] + [[product.name, product.price, product.qty] for product in magazine]
        # print(to_table)
        print(tabulate(to_table, headers='firstrow', tablefmt='github', showindex='always'))

        # print(list(magazine))
        choice = int(input('\nPodaj nr produktu: '))
        print(magazine[choice-1])
        input('It\'s \u1278')
        input("It's \u1278")