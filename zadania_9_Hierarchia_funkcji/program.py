import os
import random
import employees
import products
import orders
import database as dt
def options():
    cnt=0
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print_out=["Pracownicy - ","Zamówiena - ","Produkty - "]
        for i in range (3):
            if dt.auth[1][4][i]:
                print(f"{print_out[i]}{i-cnt+1}")
            else:
                cnt+=1
        try:
            option = int(input("\ninput: "))
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"ERROR: Proszę wprowadzić cyfrę z przedziału {1} - {i-cnt+1}")
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


option = None
while True:
    if dt.auth[0] == False:
        employees.login()
    elif dt.auth[0] == True:
        if (bool(dt.auth[1][4][0]) + bool(dt.auth[1][4][1]) + bool(dt.auth[1][4][2]))>1:
                option=options()
                if option == 0:
                    employees.menu()
            
    elif dt.auth[0] == None:
        break
        



