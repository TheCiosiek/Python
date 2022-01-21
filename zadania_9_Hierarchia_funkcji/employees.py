import random
import os
import database as dt
import unicodedata
def menu():
    while dt.auth[0]==True:
        option = options()
        if option == 1:
            add_user()
        elif option == 2:
            del_user()
        elif option == 3:
            change_user()
        elif option == 4:
            dt.auth=False, "user"
        elif option == 5:
            dt.auth = None, "user"

def options():
    error=0
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("(1) Dodaj użytkownika\n(2) Usuń użytkownika\n(3) Zmień dane użytkownika\n(4) Wyloguj się\n(5) Wyjdź\n")
        try:
            option=int(input("input: "))
            if option not in range(1,6):
                raise ValueError
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                return option
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERROR: Wprowadzono złą wartość, spróbuj jeszcze raz.")

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("Wpisz 0, by wyjść.")
        login=input("Login: ")
        if login=="0":
            dt.auth = None, "access"
            return
        password=input("Hasło: ")
        if password=="0":
            dt.auth = None, "user"
            return
        for user in dt.users:
            if user[2].lower()==login.lower():
                if user[3]==password:
                    input("Zalogowanie poprawne. Naciśnij enter by kontynuować...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dt.auth = True, user
                    return
                else: 
                    break
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"ERROR: Nieprawidłowy login lub hasło.")

def acces_change():
    access=[]
    err=0
    while True:
        print("Dostęp do: Pracwonicy.\n0 - brak dostępu\n1 - pełny dostęp")
        try:
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 0 - 1.")
            option = int(input("\ninput: "))
            if option not in range (0,2):
                raise ValueError()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else:
            access.append(option)
            os.system('cls' if os.name == 'nt' else 'clear')
            break

    err=0
    while True:
        try:
            print("Dostęp do: Zamówienia.\n0 - brak dostępu\n1 - zamówienia/zmiana status\n2 - pełny dostęp")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 0 - 2.")
            option = int(input("\ninput: "))
            if option not in range (0,3):
                raise ValueError()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else:
            access.append(option)
            os.system('cls' if os.name == 'nt' else 'clear')
            break

    err=0  
    while True:
        try:
            print("Dostęp do: Produkty\n0 - dostęp jako klient/brak dostępu\n1 - zobaczenie dostępności produktu\n2 - pełny dostęp")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 0 - 2.")
            option = int(input("\ninput: "))
            if option not in range (0,3):
                raise ValueError()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else:
            access.append(option)
            os.system('cls' if os.name == 'nt' else 'clear')
            return access

def make_username(name,surname):
    #zmiana z ł na l, ponieważ normalize() nie potrafi
    name = name.replace("ł", "l")
    name = name.replace("Ł", "l")
    #normalize 'Szyłak'->kody unicode->b'Szyak'->'Szylak' 
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode("utf-8")

    surname = surname.replace("ł", "l")
    surname = surname.replace("Ł", "l")
    surname = unicodedata.normalize('NFKD', surname).encode('ascii', 'ignore').decode("utf-8")

    username=""
    i=0
    #try i except jakby imię lub nazwisko było krótsze niż 3
    try:
        while i<3:
            username+=name[i].lower()
            i+=1
    except IndexError:
        pass
    i=0
    try:
        while i<3:
            username+=surname[i].lower()
            i+=1
    except IndexError:
        pass
    return username

def add_user():
    print("Wpisz 0, by wyjść")
    while True:
        name = input("Wprowadź imię: ")
        if name==0:
            return
        if name.isalpha():
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERORR: Imię może zawierać tylko litery. Wpisz 0, by wyjść.")
    print("Wpisz 0, by wyjść")
    while True:
        surname = input("Wprowadź nazwisko: ")
        if surname==0:
            return
        if surname.isalpha():
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERORR: Nazwisko może zawierać tylko litery. Wpisz 0, by wyjść.")
    i=0
    username = make_username(name, surname)
    access = acces_change()
    password =""
    for i in range (8):
        password += random.choice(random.choice(["abcdefghijlklmnopqrstuvwxyz","ABCDEFGHIJLKMNOPQRSTUVWXYZ","123456789","~`!@#$%^&*()_-+="]))
    input(f"Utworzona nazwa użytkownika: {username}\nUtworzone hasło: {password}\nDostęp:\n  Pracownicy - {access[0]}\n  Zamówienia - {access[1]}\n  Produkty - {access[2]}\n\nWprowadź enter by kontynuować...")
    dt.users.append([name, surname, username, password, access])
    return

def del_user():
    err=0
    del_user=""
    while del_user!="0":
        os.system('cls' if os.name == 'nt' else 'clear')
        for user in dt.users:
            print(f"imię: {user[0]}, nazwisko: {user[1]}, nazwa: {user[2]}")
        if err==1:
            print("ERROR: Nie znaleziono użytkownika. Wpisz 0, by wyjść.")
        else:
            print("Wpisz 0, by wyjść.")
        del_user = input("\nNazwa użytkownika do usunięcia: ")
        if del_user == "0":
            return
        i=0
        for user in dt.users:
            if user[2] == del_user:
                del dt.users[i]
                input("Usuwanie użytkownika poprawne. Wprowadź enter by kontynuować...")
                return
            i+=1
        err=1


def change_user():
    err=0
    #Wysukiwanie użytkownika
    while True:
        for user in dt.users:
            print(f"imię: {user[0]}, nazwisko: {user[1]}, nazwa: {user[2]}, hasło: {user[3]}, dostęp: {user[4]}")
        if err==0:
            print("Wpisz 0, by wyjść.")
        else:
            print("ERROR: Nie znaleziono użytkownika. Wpisz 0, by wyjść.")
        change_user = input("\nNazwa użytkownika do zmiany: ")
        for user in dt.users:
            if user[2] == change_user:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
    #Zmiana użytkownika        
    print("\n1 - imię\n2 - nazwisko\nnazwa użytkownika - 3\nhasło - 4\ndostęp - 5")
    if err==1:
        print("ERROR: Wprowadź cyfrę z przedziału 1 - 5. Wpisz 0, by wyjść.")
    else:
        print("Wpisz 0, by wyjść.")
    try:
        option = int(input("\ninput: "))
        if option not in range (1, 6):
            raise ValueError()
    except ValueError:
        err=1
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    print