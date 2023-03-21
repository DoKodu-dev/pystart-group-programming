## Zadanie
Napisz program w Pythonie, który będzie symulować działanie sklepu internetowego. Program powinien pozwalać
użytkownikowi na dodawanie produktów do koszyka, wyświetlanie ich listy wraz z cenami i obliczanie łącznej wartości
zamówienia. Program powinien również umożliwiać wprowadzenie danych klienta, takich jak imię, nazwisko, adres i numer
telefonu.

## Wymagania
[ ] Program powinien składać się z co najmniej dwóch klas: Produkt i Koszyk.

[ ] Klasa Produkt powinna zawierać pola nazwa i cena.

[ ] Klasa Koszyk powinna zawierać metody dodaj_produkt(produkt: Produkt, ilosc: int) oraz pokaz_koszyk(), które pozwolą użytkownikowi na dodanie produktów do koszyka oraz wyświetlenie ich listy wraz z cenami.

[ ] Program powinien umożliwiać użytkownikowi wprowadzenie danych klienta, takich jak imię, nazwisko, adres i numer telefonu, oraz wyświetlenie ich na ekranie wraz z łączną wartością zamówienia.

[ ] Program powinien działać w nieskończoność, dopóki użytkownik nie zdecyduje się zakończyć jego działania.

## Output
```Podaj swoje imię: Jan
Podaj swoje nazwisko: Kowalski
Podaj swój adres: ul. Wiejska 1, 00-001 Warszawa
Podaj swój numer telefonu: 123-456-789

Witaj, Jan Kowalski!

Oto lista produktów:
1. Myszka komputerowa - 49.99 zł
2. Klawiatura - 99.99 zł
3. Monitor - 699.99 zł
4. Kamera internetowa - 149.99 zł

Podaj numer produktu, który chcesz dodać do koszyka (lub wpisz 'q', aby zakończyć): 1
Podaj ilość: 2
Produkt dodany do koszyka.

Podaj numer produktu, który chcesz dodać do koszyka (lub wpisz 'q', aby zakończyć): 3
Podaj ilość: 1
Produkt dodany do koszyka.

Podaj numer produktu, który chcesz dodać do koszyka (lub wpisz 'q', aby zakończyć): q

Twoje zamówienie:
------------------
Myszka komputerowa x 2 - 99.98 zł
Monitor x 1 - 699.99 zł
------------------
Łączna wartość zamówienia: 799.97 zł

Dane klienta:
--------------
Imię i nazwisko: Jan Kowalski
Adres: ul. Wiejska 1, 00-001 Warszawa
Numer telefonu: 123-```