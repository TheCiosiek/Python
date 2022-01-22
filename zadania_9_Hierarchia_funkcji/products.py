import os
import data as dt

def options():
    error=0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("(1) Dodaj zamówienie\n(2) Usuń zamówienie\n(3) Wyszukaj zamówienie\n(4) Zmień zamówienie.")
        try:
            if error==1:
                print("ERROR: Wprowadzono złą wartość, spróbuj jeszcze raz.")
            option=int(input("input: "))
            if option not in range(1,5):
                raise ValueError
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                return option
        except ValueError:
            error=1

def menu():
    dt.load_products()
    while dt.auth[0]==True:
        option = options()
        if option == 1:
            add_order()
        elif option == 2:
            del_order()
        elif option == 3:
            change_order()
        elif option == 4:
            dt.auth=False, "user"
        elif option == 5:
            dt.auth = None, "user"

def print_list():
    for item in dt.products():
        print(f"sztuk ryz: {item[0]}\nformat: A{item[1]}\ngramatura: {item[2]}g/m\nnazwa: {item[3]}\nproducent: {item[4]}")
        
def add_order():
    print_list()
    