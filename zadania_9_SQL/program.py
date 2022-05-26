import os
import random
import employees
import products
import orders
import data as dt
import sqlite3
from datetime import datetime

def options():
    err=0
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        cnt=0
        print_out=["Pracownicy - ","Produkty   - ","Zamówienia - "]
        for i in range (3):
            if dt.auth[2][i]:
                print(f"{print_out[i]}{i-cnt+1}")
            else:
                cnt+=1
        if err==1:
            print(f"ERROR: Wprowadź cyfrę z przedziału {1} - {3-cnt}")
        try:
            option = int(input("\ninput: "))
            if option not in range (1, i-cnt+2):
                raise ValueError()
        except ValueError:
            err=1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    i=0
    cnt=0
    while i<len(dt.auth[2]):
        if dt.auth[2][i]:
            cnt+=1
            if cnt==option:
                return i
        i+=1

def login():
    DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
    conn = sqlite3.connect(DATA_PATH)
    curs = conn.cursor()  

    users = curs.execute('SELECT * from users').fetchall()
    users_access = curs.execute('SELECT users, products, orders from users_access').fetchall()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("Wpisz 0 by wyjść.")
        login=input("Login: ")
        if login=="0":
            dt.auth = None, "access"
            return
        password=input("Hasło: ")
        if password=="0":
            dt.auth = None, "user"
            return
        for user in users:
            if user[2].lower()==login.lower():
                if user[3]==password:
                    input("Zalogowanie poprawne. Naciśnij enter by kontynuować...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dt.auth = True, user[2], users_access[0]
                    curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Użytkownik się zalogował"))
                    conn.commit()
                    conn.close()
                    return
                else: 
                    break
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"ERROR: Nieprawidłowy login lub hasło.")

option = None
while True:
    if dt.auth[0] == False:
        login()
    elif dt.auth[0] == True:
        if (dt.auth[2][0] + dt.auth[2][1] + dt.auth[2][2])>1:
                option=options()
                if option == 0:
                    employees.menu()
                elif option == 1:
                    products.menu()
                else:
                    orders.menu()
        elif dt.auth[2][0]:
            employees.menu()
        elif dt.auth[2][1]:
            products.menu()
        else:
            orders.menu()
    elif dt.auth[0] == None:
        break
        



