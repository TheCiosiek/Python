import random
import os
import sqlite3
from typing import Optional
import unicodedata
import pandas as pd
from datetime import datetime
import data as dt
from pydantic import BaseModel, ValidationError, root_validator, validator

def menu():
    while dt.LoggedUserObj.logged==True:
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
            dt.LoggedUserObj.logged=False
        elif option == 6:
            dt.LoggedUserObj.logged = None

def options():
    err=0
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        if (dt.LoggedUserObj.access_list[0] + dt.LoggedUserObj.access_list[1] + dt.LoggedUserObj.access_list[2])>1:
            print("(1) Dodaj użytkownika\n(2) Usuń użytkownika\n(3) Zmień użytkownika\n(4) Zmień program\n(5) Wyloguj się\n(6) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 6.")
        else:
            print("(1) Dodaj użytkownika\n(2) Usuń użytkownika\n(3) Zmień użytkownika\n(4) Wyloguj się\n(5) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 5.")
        try:
            option=int(input("\ninput: "))
            if (dt.LoggedUserObj.access_list[0] + dt.LoggedUserObj.access_list[1] + dt.LoggedUserObj.access_list[2])>1:
                if option not in range(1, 7):
                    raise ValueError
            else:
                if option not in range(1, 6):
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
            access.append(bool(option))
            os.system('cls' if os.name == 'nt' else 'clear')
            break

    err=0  
    while True:
        try:
            print("Dostęp do: Produkty\n0 - brak dostępu\n1 - dostęp")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 0 - 1.")
            option = int(input("\ninput: "))
            if option not in range (0,2):
                raise ValueError()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else:
            access.append(bool(option))
            os.system('cls' if os.name == 'nt' else 'clear')
            break

    err=0
    while True:
        try:
            print("Dostęp do: Zamówienia.\n0 - brak dostępu\n1 - dostęp")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 0 - 1.")
            option = int(input("\ninput: "))
            if option not in range (0,2):
                raise ValueError()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else:
            access.append(bool(option))
            os.system('cls' if os.name == 'nt' else 'clear')
            return access

def make_username(name, surname, users):
    #zmiana z ł na l, ponieważ normalize() nie potrafi
    name = name.replace("ł", "l")
    name = name.replace("Ł", "l")
    #gdyby nie linijka wyżej byłoby, ponieważ nie ma "ł": normalize 'Szyłak'->kody unicode->b'Szyak'->'Szylak' 
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
    for user in users:
        if user==username:
            i+=1
            #sprawdzenie każdej kolejnej liczby czy już taka istnieje
            while cont==1:
                cont=0
                for user in users:
                    if user==username+("_"+str(i)):
                        i+=1
                        cont=1
                        break
            break         
    if i>1:
        username+=("_"+str(i))
    return username


class UserCheck(BaseModel):
    name: Optional[str]
    password: Optional[str]
    passLength: bool = False
    passBigLetters : bool = False
    passSmallLetters : bool = False
    passDigits: bool = False
    passSpecial: bool = False

    @validator("name")
    def alpha_check(cls, v):
        if not v.isalpha():
            raise ValueError("alpha")
        else:
            return v
        
    @validator("name")
    def check_length(cls, v):
        if len(v) >= 50:
            raise ValueError("length")
        return v
    
    @root_validator
    def passValidator(cls, values):
        password = values.get("password")
        if password is not None:
            if len(password) >= 8:
                values['passLength'] = True 
            for i in password:
                if i.isalpha():
                    if ord(i) in range(65,91):
                        values['passBigLetters'] = True
                    else:
                        values['passSmallLetters'] = True
                elif i.isdigit():
                    values['passDigits'] = True
                else:
                    values['passSpecial'] = True
            return values


def add_name():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Wpisz 0, by wyjść")
    while True:
        name = input("\nWprowadź imię: ")
        if name=="0":
            return "0"
        try:
            UserCheck(name=name)
        except ValueError as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            if e.args[0][0].exc.args[0] == "length":
                print("ERROR: Imię musi mieć najwyżej 50 znaków.")
            elif e.args[0][0].exc.args[0] == "alpha":
                print("ERROR: Imię musi składać się tylko z liter.")
        else:
            return name

def add_surname():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Wpisz 0, by wyjść")
    while True:
        surname = input("\nWprowadź nazwisko: ")
        if surname=="0":
            return "0"
        try:
            UserCheck(name=surname)
        except ValueError as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            if e.args[0][0].exc.args[0] == "length":
                print("ERROR: Nazwisko musi mieć najwyżej 50 znaków.")
            elif e.args[0][0].exc.args[0] == "alpha":
                print("ERROR: Nazwisko musi składać się tylko z liter.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            return surname

def add_user():
    
    DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
    conn = sqlite3.connect(DATA_PATH)
    curs = conn.cursor()

    queryset = curs.execute('SELECT username from users')
    users = queryset.fetchall()
    i=0
    for user in users:
        users[i] = user[0]
        i += 1

    name = add_name()
    if name == "0":
        return

    surname = add_surname()
    if surname == "0":
        return

    i=0
    username = make_username(name, surname, users)
    access = acces_change()
    password =""

    for i in range (8):
        password += random.choice(random.choice(["abcdefghijlklmnopqrstuvwxyz","ABCDEFGHIJLKMNOPQRSTUVWXYZ","123456789","~`!@#$%^&*()_-+="]))
    curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.LoggedUserObj.username, "Dodano użytkownika " + username))
    curs.execute('INSERT INTO users VALUES (?, ?, ?, ?)', (name, surname, username, password))
    curs.execute('INSERT INTO users_access VALUES (?, ?, ?, ?)', (username, access[0], access[1], access[2]))
    conn.commit()
    conn.close()
    input(f"Utworzona nazwa użytkownika: {username}\nUtworzone hasło: {password}\nDostęp:\n  Pracownicy - {access[0]}\n  Zamówienia - {access[1]}\n  Produkty - {access[2]}\n\nWprowadź enter by kontynuować...")
    return

def del_user():
    err=0
    del_user=""
    DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
    conn = sqlite3.connect(DATA_PATH)
    curs = conn.cursor()
    queryset = curs.execute('SELECT name, surname, username from users')
    users = queryset.fetchall()

    os.system('cls' if os.name == 'nt' else 'clear')
    df = pd.DataFrame(data = users, columns=["Imię","Nazwisko", "Nazwa"])
    #zmienienie do lewej strony
    
    if df.empty:
        input("ERROR: W bazie nie ma żadnego użytkownika. Wprowadź enter by kontynuować...")
        return

    #Gdyby było SELECT * FROM users
    # df = pd.DataFrame(data = users, columns=["Imię","Nazwisko","Nazwa","Hasło"]).loc[:, ["Imię", "Nazwisko", "Nazwa"]]

    while del_user!="0":
        #
        print(df.to_string(index=False))
        print()

        if err==1:
            print("ERROR: Nie znaleziono użytkownika. Wpisz 0, by wyjść.")
        else:
            print("Wpisz 0, by wyjść.")

        del_user = input("Nazwa użytkownika do usunięcia: ")
        if del_user == "0":
            return

        i=0
        for user in users:
            if user[2].lower() == del_user.lower():
                curs.execute('DELETE FROM users WHERE username = ?', (user[2],))
                curs.execute('DELETE FROM users_access WHERE username = ?', (user[2],))

                curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.LoggedUserObj.username, "Usunięto użytkownika " + del_user))

                conn.commit()
                conn.close()
                input("Usuwanie użytkownika poprawne. Wprowadź enter by kontynuować...")
                return
            i+=1
        err=1

def add_username(users):
    err=0
    while True:
        if err==1:
            print("ERROR: Login już istnieje. Wpisz 0 by wyjść.")
            err=0

        elif err==2:
            print("ERROR: Login ma mniej niż 6 znaków. Wpisz 0 by wyjść.")
            err=0

        elif err==3:
            print("ERROR: Login ma więcej niż 30 znaków. Wpisz 0 by wyjść.")
            err=0

        else:
            print("Login musi mieć między 6, a 30 znaków. Wpisz 0 by wyjść.")
        username=input("\nWprowadź login: ")
        
        if username=="0":
            os.system('cls' if os.name == 'nt' else 'clear')
            return "0"

        elif len(username)<6:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=2
            continue

        elif len(username)>30:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=3
            continue

        for user in users:
            if user[2].lower()==username.lower():
                os.system('cls' if os.name == 'nt' else 'clear')
                err=1
        if err==0:
            return username

def add_password():
    while True:
        all_ok=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Hasło musi mieć przynajmniej 8 znaków, jedną małą i dużą literę, cyfrę oraz znak. Wpisz 0 by wyjść.")
        password=input("Wprowadź hasło: ")
        if password=="0":
            return "0"
        else:
            userChecked = UserCheck(password=password)
            password_pass={"Osiem znaków":userChecked.passLength,"Duże litery":userChecked.passBigLetters,"Małe litery":userChecked.passSmallLetters,"Cyfry":userChecked.passDigits,"Znaki specjalne":userChecked.passSpecial}
        s=" "
        for i in password_pass:
            if not password_pass[i]:
                ok=False
                all_ok=0
            else:
                ok=True
            print (f"{i}:{s*(17-len(i))} {ok}")        
        if not all_ok:
            input(f"ERROR: Hasło nie spełnia wymagań. Wprowadź enter by kontynuować...")
        else: 
            input(f"Hasło poprawne. Wprowadź enter by kontynuować...")
            os.system('cls' if os.name == 'nt' else 'clear')
            return password

def change_user():
    err=0
    cont=1
    DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
    conn = sqlite3.connect(DATA_PATH)
    curs = conn.cursor()

    queryset = curs.execute('SELECT * from users')
    users = queryset.fetchall()

    queryset = curs.execute('SELECT * from users_access')
    users_access = queryset.fetchall()

    #Wysukiwanie użytkownika
    while cont:
        df = pd.DataFrame(data = users, columns=["Imię","Nazwisko","Nazwa","Hasło"])
        df2 = pd.DataFrame(data = users_access, columns=["Nazwa","Dostęp_pracownicy","Dostęp_produkty","Dostęp_zamówienia"])
        df["Dostęp_pracownicy"], df["Dostęp_produkty"], df["Dostęp_zamówienia"] =  df2["Dostęp_pracownicy"].astype('bool'), df2["Dostęp_produkty"].astype('bool'), df2["Dostęp_zamówienia"].astype('bool')
        
        if df.empty:
            input("ERROR: W bazie nie ma żadnego użytkownika. Wprowadź enter by kontynuować...")
            return
        print(df.to_string(index=False))
        print()
        if err==0:
            print("Wpisz 0, by wyjść.")
        else:
            print("ERROR: Nie znaleziono użytkownika. Wpisz 0, by wyjść.")
        change_user = input("Nazwa użytkownika do zmiany: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        if change_user == "0":
            return
        
        #szukanie użytkownika
        i=0
        while i<len(users):
            if users[i][2].lower() == change_user.lower():
                cont = 0
                user = df.iloc[i]
                break
            i+=1
        err=1
    #Zmiana użytkownika
    err=0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        username = users[i][2]
        print(user.to_string())
        # print(f"imię: {users[i][0]}, nazwisko: {users[i][1]}, nazwa: {users[i][2]}, hasło: {users[i][3]}, dostęp: {users[i][4]}")
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
            if option==0:
                break
            os.system('cls' if os.name == 'nt' else 'clear')

            if option==1:
                name = add_name()
                if name == "0":
                    continue
                curs.execute('UPDATE users SET name = ? WHERE username = ?', (name, username))
                curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.LoggedUserObj.username, "Zmieniono imię użytkownika " + change_user))
                user[0] = name
                dt.LoggedUserObj.name = name
                os.system('cls' if os.name == 'nt' else 'clear')

                if input("Zmienić nazwę użytkownika?\n0 - nie\n1 - tak\n\ninput: ") == "1":
                    new_username = make_username(name, users[i][1], users)
                    curs.execute('UPDATE users SET username = ? WHERE username = ?', (new_username, username))
                    curs.execute('UPDATE users_access SET username = ? WHERE username = ?', (new_username, username))
                    curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.LoggedUserObj.username, "Zmieniono nazwę użytkownika " + change_user))
                    user[2] = new_username
                    dt.LoggedUserObj.username = new_username
                conn.commit()

            elif option==2:
                surname = add_surname()
                if surname == "0":
                    continue
                curs.execute('UPDATE users SET surname = ? WHERE username = ?', (surname, username))
                curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.LoggedUserObj.username, "Zmieniono nazwisko użytkownika " + change_user))
                user[1] = surname
                dt.LoggedUserObj.surname = surname
                os.system('cls' if os.name == 'nt' else 'clear')

                if input("Zmienić nazwę użytkownika?\n0 - nie\n1 - tak\n\ninput: ") == "1":
                    new_username = make_username(name, users[i][1], users)
                    curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.LoggedUserObj.username, "Zmieniono nazwę użytkownika " + change_user))
                    curs.execute('UPDATE users SET username = ? WHERE username = ?', (new_username, username))
                    curs.execute('UPDATE users_access SET username = ? WHERE username = ?', (new_username, username))
                    user[2] = new_username
                conn.commit()

            elif option==3:
                new_username = add_username(users)
                if new_username == "0":
                    continue
                curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.LoggedUserObj.username, "Zmieniono nazwę użytkownika " + change_user))
                curs.execute('UPDATE users SET username = ? WHERE username = ?', (new_username, username))
                curs.execute('UPDATE users_access SET username = ? WHERE username = ?', (new_username, username))
                conn.commit()
                user[2] = new_username
                dt.LoggedUserObj.username = new_username
                continue

            elif option==4:
                password = add_password()
                if password == "0":
                    continue
                curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.LoggedUserObj.username, "Zmieniono hasło użytkownika " + change_user))
                curs.execute('UPDATE users SET password = ? WHERE username = ?', (password, username))
                conn.commit()
                user[3] = password
            elif option==5:
                new_access = acces_change()
                curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.LoggedUserObj.username, "Zmieniono dostęp użytkownika " + change_user))
                curs.execute('UPDATE users_access SET users = ?, products = ?, orders = ? WHERE username = ?', (new_access[0], new_access[1], new_access[2], username))
                conn.commit()
                user[4], user[5], user[6] = new_access[0], new_access[1], new_access[2]
                
    conn.close()
    input("Zmiana użytkownika poprawna. Wprowadź enter by kontynuować...")
    os.system('cls' if os.name == 'nt' else 'clear')