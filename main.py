'''
lista produktów
koszyk
- dodawanie produktów
- pokazywanie stanu koszyka
dane klienta (imie, nazwisko, adres, nr tel)
'''
produkty = {
    "Myszka komputerowa": {
        'cena': 49.99,
        'ilosc': 5
    },
    "Klawiatura": {
        "cena": 99.99,
        "ilosc": 10
    },
    "Monitor": {
        "cena": 699.99,
        "ilosc": 3
    },
    "Kamera internetowa": {
        "cena": 149.99,
        "ilosc": 7
    }
}


def dodaj_produkt(nazwa: str, ilosc: int, koszyk: list = None, lista_produktow: dict = produkty) -> list:
    if not koszyk:
        koszyk = []

    if nazwa in lista_produktow.keys():
        cena = lista_produktow[nazwa]['cena']
        dostepna_ilosc = lista_produktow[nazwa]['ilosc']
        if dostepna_ilosc >= ilosc:
            koszyk.append((nazwa, ilosc, cena))
            print('-- Dodano do koszyka --')
        else:
            print(
                f'Brak wystarczajacej ilości w magazynie!! - na stanie mamy {dostepna_ilosc}')

    return koszyk


def pokaz_koszyk(koszyk: list = None) -> None:
    if koszyk:
        suma_koszyka = 0
        print("Twoje zamówienie: ")
        print("-"*10)
        for produkt in koszyk:
            print(f'{produkt[0]} - {produkt[1]*produkt[2]} zł')
            suma_koszyka += produkt[1] * produkt[2]
        print("-"*10)
        print(f'Łączna wartosc zamówienia: {suma_koszyka:.2f}')


if __name__ == '__main__':
    koszyk = []
    while True:
        for numer, produkt in enumerate(produkty.items(), start=1): # (nr, (klucz, wartosc))
            print(f'{numer} - {produkt[0]} - {produkt[1]["cena"]} PLN')
        print(f'0 - zakończ dodawanie produktów do koszyka')

        numer_produktu = int(
            input('\n\n\tPodaj nr produktu, który chcesz dodać do koszyka: '))
        if numer_produktu == 0:
            pokaz_koszyk(koszyk)
            break

        ilosc = int(input('\tPodaj ilość: '))
        koszyk = dodaj_produkt(
            list(produkty.keys())[numer_produktu-1],
            ilosc,
            koszyk
        )


# przenieść magazyn do BD (sqlite3)
# przepisać na OOP
# testy
# pydocs
# wyjatki 