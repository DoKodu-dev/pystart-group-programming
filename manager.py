'''
- Dodawanie nowego pracownika
- Usuwanie istniejącego pracownika
- Edycja danych pracownika
- Wyszukiwanie pracownika na podstawie imienia, nazwiska, stanowiska lub adresu e-mail
- Wyświetlanie wszystkich pracowników w systemie

TKinter, CSV

employee = [id, name, last_name, date, positon, email, phone]
'''
import datetime
import csv

def gui_app() -> None:
    pass

def add_employee(name: str, last_name: str, date: datetime.date, positon: str, email: str, phone: int) -> str:
    list_of_employee = read_data()
    try:
        empl_id = list_of_employee[-1][0] + 1
    except IndexError:
        empl_id = 1

    list_of_employee.append([empl_id, name,last_name,date,positon,email,phone]) 
    communicate = save_data(list_of_employee)
    return communicate


# def remove_employee(id: int) -> str:
#     list_of_employee = read_data()
#     list_employee.
#     return str(communicate)

# def list_employee() -> list:
#     return list_of_employee


# def edit_employee(id: int, name: str, last_name: str, date: date, positon: str, email: str, phone: int) -> str:
#     return str(communicate)

# def search_employee(name: str = None, last_name: str = None, date: date = None, positon: str = None, email: str = None, phone: int = None) -> list:
#     return list_of_employee


def read_data() -> list:
    try:
        with open('employees.csv') as csv_file:
            list_of_employee = csv.reader(csv_file, delimiter=',', quotechar='"')
    except FileNotFoundError:
        return []

    return list_of_employee

def save_data(list_of_employees: list) -> str:
    try:
        with open('employees.csv', mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')
            csv_writer.writerows(list_of_employees)
    except:
        return 'Coś poszło nie tak'
    return 'Wszystko OK'


if __name__ == '__main__':
    name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")
    date = input("Podaj datę urodzenia [DD.MM.RRRR]: ").split('.')
    position = input("Podaj stanowisko: ")
    email = input("Podaj adres e-mail: ")
    phone = int(input("Podaj numer telefonu: ")) # typ int
    date = [int(i) for i in date] # list comprehension
    date = datetime.date(day=date[0], month=date[1], year=date[2])

    add_employee(name, last_name, date, position, email, phone)