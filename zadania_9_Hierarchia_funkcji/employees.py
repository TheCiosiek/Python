import random
import os
import database as dt
def menu():
    option = options()
    if option == 1:
        add_user()
    elif option == 2:
        #del_user()
        TODO
    elif option == 3:
        #change_user()
        TODO
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
    while True:
        try:
            temp = int(input("Dostęp do: Pracwonicy.\n0 - brak dostępu\n1 - pełny dostęp\n\ninput: "))
            if temp not in range (0,2):
                raise ValueError()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERROR: Proszę wprowadzić cyfrę z przedziale 0 - 1")
        else:
            access.append(temp)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    while True:
        try:
            temp = int(input("Dostęp do: Zamówienia.\n0 - brak dostępu\n1 - zamówienia/zmiana status\n2 - pełny dostęp\n\ninput: "))
            if temp not in range (0,3):
                raise ValueError()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERROR: Proszę wprowadzić cyfrę z przedziale 0 - 2")
        else:
            access.append(temp)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    while True:
        try:
            temp = int(input("Dostęp do: Produkty\n0 - dostęp jako klient/brak dostępu\n1 - zobaczenie dostępności produktu\n2 - pełny dostęp\n\ninput: "))
            if temp not in range (0,3):
                raise ValueError()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERROR: Proszę wprowadzić cyfrę z przedziale 0 - 2")
        else:
            access.append(temp)
            os.system('cls' if os.name == 'nt' else 'clear')
            return access

def add_user():
    while True:
        name = input("Wprowadź imię: ")
        if name.isalpha():
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("ERORR: Imię może zawierać tylko litery")
    while True:
        surname = input("Wprowadź nazwisko: ")
        if surname.isalpha():
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("ERORR: Nazwisko może zawierać tylko litery")
    i=0
    username=""
    try:
        while i<3:
            username+=name[i].lower()
            i+=1
    except:
        pass
    i=0
    try:
        while i<3:
            username+=surname[i].lower()
            i+=1
    except:
            pass
    access = acces_change()
    password =""
    for i in range (8):
        password += random.choice(random.choice(["abcdefghijlklmnopqrstuvwxyz","ABCDEFGHIJLKMNOPQRSTUVWXYZ","123456789","~`!@#$%^&*()_-+="]))
    input(f"Utworzona nazwa użytkownika: {username}\nUtworzone hasło: {password}\nDostęp:\n  Pracownicy - {access[0]}\n  Zamówienia - {access[1]}\n  Produkty - {access[2]}\nWprowadź enter by kontynuować...")
    dt.users.append([name, surname, username, password, access])
    return
