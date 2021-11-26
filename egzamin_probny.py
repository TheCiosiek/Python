class animal():
    def __init__(self,name):
        self.name=name
    def get_name():
        pass
    def set_name():
        pass
class Mammal(animal):
    def __init_(self,name, no_legs,has_fur):
        self.no_leg=no_leg
        self.has_fur=has_fur
    def get_no_legs():
        pass
    def set_no_legs():
        pass
    def get_has_fur():
        pass
    def set_has_fur():
        pass
class Canine(Mammal):
    def __init_(self,name, no_legs,has_fur):
        pass
    def howl():
        pass
    def bark():
        pass
class dog(Canine):
    def __init_(self,name, no_legs,has_fur,kind,owner):
        self.owner=owner
        self.kind=kind
    def get_kind():
        pass
    def set_kind():
        pass
    def get_owner():
        pass
    def set_owner():
        pass        
#------------------------------------------------------^ZADANIE 6^
import math

def calc_circle_area(n):
    area=(math.pi)*n**2
    return area

r=float(input("Wprowadź promień: "))
area=calc_circle_area(r)
print(area)
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
slownik = {}

def print_menu():
    print('1. Dodaj wpis')
    print('2. Odzyskaj wpis')
    print('3. Zmodyfikuj wpis')
    print('4. Usu? wpis')
    print('0. Wyjd?')
    
def create_item(slownik):
    while True:
        print("Podaj nowy klucz i wartość")
        new_key=input("Nowy klucz: ")
        try:
            if new_key in slownik:
                print("Klucz już istnieje, spróbuj jeszcze raz")
            else:
                raise TypeError
        except TypeError:
            new_value=input("Nowa wartość: ")
            slownik[new_key]=new_value
            break
    return slownik
def read_item(slownik):
    while True:
        try:
            find_key=input("Wprowadź klucz z którego chcesz odczytać wartość: ")
            if find_key in slownik:
                print(f"Wartość: {slownik[find_key]}")
                input("Wprowadź dowolny klawisz by kontynuować")
                break
            else:
                raise TypeError
        except TypeError:
            print("Klucz nie znajduje się w słowniku, spróbuj jeszcze raz.")
def update_item(slownik):
    while True:
        try:
            find_key=input("Wprowadź klucz, którego wartość chcesz zmienić: ")
            if find_key in slownik:
                new_value=input("Wprowadź nową wartość: ")
                slownik[find_key]=new_value
                break
            else:
                raise TypeError
        except TypeError:
            print("Klucz nie znajduje się w słowniku, spróbuj jeszcze raz.")
    return slownik
def delete_item(slownik):
    while True:
        try:
            find_key=input("Wprowadź klucz, który chcesz usunąć: ")
            if find_key in slownik:
                del slownik[find_key]
                break
            else:
                raise TypeError
        except TypeError:
            print("Klucz nie znajduje się w słowniku, spróbuj jeszcze raz.")
    return slownik
while True:
    print_menu()
    option = input("Podaj opcj?: ")
    if option == '1':
        slownik=create_item(slownik)
    elif option == '2':
        read_item(slownik)
    elif option == '3':
        slownik=update_item(slownik)
    elif option == '4':
        slownik=delete_item(slownik)
    elif option == '0':
        break
