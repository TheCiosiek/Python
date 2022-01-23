import random
import os
import data as dt
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
            return
        elif option == 5:
            dt.auth=False, "user"
        elif option == 6:
            dt.auth = None, "user"

def options():
    err=0
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        if (bool(dt.auth[1][4][0]) + bool(dt.auth[1][4][1]) + bool(dt.auth[1][4][2]))>1:
            print("(1) Dodaj użytkownika\n(2) Usuń użytkownika\n(3) Zmień dane użytkownika\n(4) Zmień program\n(5) Wyloguj się\n(6) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 6.")
        else:
            print("(1) Dodaj użytkownika\n(2) Usuń użytkownika\n(3) Zmień dane użytkownika\n(4) Wyloguj się\n(5) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 5.")
        try:
            option=int(input("\ninput: "))
            if (bool(dt.auth[1][4][0]) + bool(dt.auth[1][4][1]) + bool(dt.auth[1][4][2]))>1:
                if option not in range(1,7):
                    raise ValueError
            else:
                if option not in range(1,6):
                    raise ValueError
                elif option >3:
                    option+=1
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            return option

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
    i=1
    cont=1
    #sprawdzenie czy istnieje nazwa bez liczby
    for user in dt.users:
        if user[2]==username:
            i+=1
            #sprawdzenie każdej kolejnej liczby czy już taka istnieje
            while cont==1:
                cont=0
                for user in dt.users:
                    if user[2]==username+("_"+str(i)):
                        i+=1
                        cont=1
                        break
            break
                
    if i>1:
        username+=("_"+str(i))
    return username

def add_name():
    print("Wpisz 0, by wyjść")
    while True:
        name = input("Wprowadź imię: ")
        if name=="0":
            return "0"
        if name.isalpha():
            os.system('cls' if os.name == 'nt' else 'clear')
            return name
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERORR: Imię może zawierać tylko litery. Wpisz 0, by wyjść.")

def add_surname():
    print("Wpisz 0, by wyjść")
    while True:
        surname = input("Wprowadź nazwisko: ")
        if surname=="0":
            return "0"
        if surname.isalpha():
            os.system('cls' if os.name == 'nt' else 'clear')
            return surname
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERORR: Nazwisko może zawierać tylko litery. Wpisz 0, by wyjść.")

def add_user():
    name = add_name()
    if name == "0":
        return
    surname = add_surname()
    if surname == "0":
        return
    i=0
    username = make_username(name, surname)
    access = acces_change()
    password =""
    for i in range (8):
        password += random.choice(random.choice(["abcdefghijlklmnopqrstuvwxyz","ABCDEFGHIJLKMNOPQRSTUVWXYZ","123456789","~`!@#$%^&*()_-+="]))
    input(f"Utworzona nazwa użytkownika: {username}\nUtworzone hasło: {password}\nDostęp:\n  Pracownicy - {access[0]}\n  Zamówienia - {access[1]}\n  Produkty - {access[2]}\n\nWprowadź enter by kontynuować...")
    dt.users.append([name, surname, username, password, access])
    dt.write_users()
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
                dt.write_users()
                input("Usuwanie użytkownika poprawne. Wprowadź enter by kontynuować...")
                return
            i+=1
        err=1

def add_username():
    err=0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Login musi mieć przynajmniej 6 znaków. Wpisz 0, by wyjść.")
        if err==1:
            print("ERROR: Login już istnieje.")
        if err==2:
            print("ERROR: Login ma mniej niż 6 znaków.")
            err=0
        username=input("\nWprowadź login: ")
        if len(username)<6:
            err=2
            continue
        if username=="0":
            return "0"
        for user in dt.users:
            if user[2]==username:
                os.system('cls' if os.name == 'nt' else 'clear')
                err==1
                break
        if err==0:
            return username


def add_password():
    while True:
        password_pass={"Sześć znaków":0,"Duże litery":0,"Małe litery":0,"Cyfry":0,"Znaki":0}
        all_ok=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Hasło musi mieć przynajmniej 8 znaków, jedną małą i dużą literę, cyfrę oraz znak. Wpisz 0 by wyjść.")
        password=input("Wprowadź hasło: ")
        if password=="0":
            return "0"
        if len(password)>7:
            password_pass["Sześć znaków"]+=1
        for i in password:
            if i.isalpha():
                if ord(i) in range(65,91):
                    password_pass["Duże litery"]+=1
                else:
                    password_pass["Małe litery"]+=1
            elif i.isdigit():
                password_pass["Cyfry"]+=1
            else:
                password_pass["Znaki"]+=1
        s=" "
        for i in password_pass:
            if password_pass[i]==0:
                ok=False
                all_ok=0
            else:
                ok=True
            print (f"{i}:{s*(12-len(i))} {ok}")        
        if not all_ok:
            input(f"ERROR: Rejestracja niepoprawna. Wprowadź enter by kontynuować...")
        else: 
            input(f"Rejestracja poprawna. Wprowadź enter by kontynuować...")
            os.system('cls' if os.name == 'nt' else 'clear')
            return password
        

def change_user():
    err=0
    cont=1
    #Wysukiwanie użytkownika
    while cont:
        for user in dt.users:
            print(f"imię: {user[0]}, nazwisko: {user[1]}, nazwa: {user[2]}, hasło: {user[3]}, dostęp: {user[4]}")
        if err==0:
            print("Wpisz 0, by wyjść.")
        else:
            print("ERROR: Nie znaleziono użytkownika. Wpisz 0, by wyjść.")
        change_user = input("\nNazwa użytkownika do zmiany: ")
        if change_user == "0":
            return
        i=0
        os.system('cls' if os.name == 'nt' else 'clear')
        while i<len(dt.users):
            if dt.users[i][2].lower() == change_user.lower():
                cont=0
                break
            i+=1
        err=1
    #Zmiana użytkownika
    err=0
    while True:
        print(f"imię: {dt.users[i][0]}, nazwisko: {dt.users[i][1]}, nazwa: {dt.users[i][2]}, hasło: {dt.users[i][3]}, dostęp: {dt.users[i][4]}")
        print("\n1 - imię\n2 - nazwisko\n3 - nazwa użytkownika\n4 - hasło\n5 - dostęp ")
        if err==1:
            print("ERROR: Wprowadź cyfrę z przedziału 0 - 5. Wpisz 0, by wyjść.")
        else:
            print("Wpisz 0, by wyjść.")
        try:
            option = int(input("\ninput: "))
            if option not in range (0, 6):
                raise ValueError()
        except ValueError:
            err=1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    if option==0:
        return
    elif option==1:
        name = add_name()
        if name == "0":
            return
        if input("Zmienić nazwę użytkownika?\n0 - nie\n1 - tak\n\ninput: ") == "1":
            dt.users[i][2] = make_username(name, dt.users[i][1])
        dt.users[i][0] = name
        dt.write_users()
    elif option==2:
        surname = add_surname()
        if surname == "0":
            return
        if input("Zmienić nazwę użytkownika?\n0 - nie\n1 - tak\n\ninput: ") == "1":
            dt.users[i][2] = make_username(dt.users[i][0], surname)
        dt.users[i][1] = surname
        dt.write_users()
    elif option==3:
        username = add_username()
        if username == "0":
            return
        dt.users[i][2]= username
        dt.write_users()
    elif option==4:
        password = add_password()
        if password == "0":
            return
        dt.users[i][3]=password
        dt.write_users()
    elif option==5:
        dt.users[i][4]= acces_change()
        dt.write_users()
    os.system('cls' if os.name == 'nt' else 'clear')
    input("Zmiana użytkownika poprawna. Wprowadź enter by kontynuować...")
#Dziękuje za dokładne sprawdzenie programu!