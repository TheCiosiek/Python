class Person():
    def __init__(self,name):
        self.name=name
    def get_name():
        pass
    def set_name():
        pass
class Employee(Person):
    def __init_(self,name, company,salary):
        self.salary=salary
        self.company=company
    def get_salary():
        pass
    def set_salary():
        pass
class Manager(Employee):
    def __init_(self,name, company,salary):
        pass
    def manage():
        pass
class Associate(Employee):
    def __init_(self,name, company,salary):
        pass
    def support():
        pass     
#------------------------------------------------------^ZADANIE 6^
import math

def calc_circle_area(n):
    area=(math.pi)*n**2
    return area

r=float(input("Wprowadź promień: "))
area=calc_circle_area(r)
print(f"{area}")
#------------------------------------------------------
def check_parity():
    number=input("wprowadź liczbę: ")
    number=int(number)
    if number%2==0:
        print("Liczba jest parzysta.")
    else:
        print("Liczba jest nieparzysta.")
check_parity()
#------------------------------------------------------
def element_present(n,tab):
    for i in tab:
        if (i==n):
            print(True)
            return True
    print(False)
    return False
n=int(input("Wprowadź liczbę: "))
tab=input("Wprowadź liczby oddzielone spacją: ").split()
tab=map(int,tab)
element_present(n, tab)
#------------------------------------------------------

def print_menu():
    print("1. Dodaj nowy samochód")
    print("2. Wyświetl samochód")
    print("3. Zmodyfikuj samochód")
    print("4. Usuń samochód")
    print("0. Wyjdź z programu")
    
def add_car(cars):
    while True:
        new_key=input("Nowy samochód: ")
        try:
            if new_key in cars:
                print("Samochód już istnieje, spróbuj jeszcze raz")
            else:
                raise TypeError
        except TypeError:
            new_value=input("Cena: ")
            cars[new_key]=new_value
            break
    return cars
def get_car(cars):
    while True:
        try:
            find_key=input("Wprowadź samochód z którego cenę chcesz odczytać: ")
            if find_key in cars:
                print(f"Cena: {cars[find_key]}")
                input("Wprowadź dowolny klawisz by kontynuować")
                break
            else:
                raise TypeError
        except TypeError:
            print("Samochód nie znajduje się w słowniku, spróbuj jeszcze raz.")
def modify_car(cars):
    while True:
        try:
            find_key=input("Wprowadź samochód, którego cene chcesz zmienić: ")
            if find_key in cars:
                new_value=input("Wprowadź nową cenę: ")
                cars[find_key]=new_value
                break
            else:
                raise TypeError
        except TypeError:
            print("Samochód nie znajduje się w słowniku, spróbuj jeszcze raz.")
    return cars
def delete_car(cars):
    while True:
        try:
            find_key=input("Wprowadź samochód, który chcesz usunąć: ")
            if find_key in cars:
                del cars[find_key]
                break
            else:
                raise TypeError
        except TypeError:
            print("Samochód nie znajduje się w słowniku, spróbuj jeszcze raz.")
    return cars
cars = {}
while True:
    print_menu()
    option = input("Podaj opcję: ")
    if option == '1':
        cars=add_car(cars)
    elif option == '2':
        get_car(cars)
    elif option == '3':
        cars=modify_car(cars)
    elif option == '4':
        cars=delete_car(cars)
    elif option == '0':
        break
