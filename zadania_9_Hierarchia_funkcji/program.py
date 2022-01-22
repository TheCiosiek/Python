import os
import random
import employees
import products
import orders
import data as dt

def options():
    err=0
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        cnt=0
        print_out=["Pracownicy - ","Zamówiena - ","Produkty - "]
        for i in range (3):
            if dt.auth[1][4][i]:
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
    while i<len(dt.auth[1][4]):
        if dt.auth[1][4][i]:
            cnt+=1
            if cnt==option:
                return i
        i+=1

def login():
    dt.load_users()
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

option = None
while True:
    if dt.auth[0] == False:
        login()
    elif dt.auth[0] == True:
        if (bool(dt.auth[1][4][0]) + bool(dt.auth[1][4][1]) + bool(dt.auth[1][4][2]))>1:
                option=options()
                if option == 0:
                    employees.menu()
                if option == 1:
                    orders.menu()
                else:
                    #products.menu()
                    pass
        elif dt.auth[1][4][0]:
            employees.menu()
        elif dt.auth[1][4][1]:
            orders.menu()
        else:
            #products.menu()
            pass
            
    elif dt.auth[0] == None:
        break
        



