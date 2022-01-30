import data as dt
import os
import orders
import pandas as pd
import numpy as np

def menu():
    dt.load_products()
    while dt.auth[0]==True:
        option = options()
        if option == 1:
            add_product()
        elif option == 2:
            change_product()
        elif option == 3:
            del_product()
        elif option == 4:
            return
        elif option == 5:
            dt.auth=False, "user"
        elif option == 6:
            dt.auth = None, "user"

def options():
    err=0
    while True:
        if (bool(dt.auth[1][4][0]) + bool(dt.auth[1][4][1]) + bool(dt.auth[1][4][2]))>1:
            print("(1) Dodaj produkt\n(2) Zmień produkt\n(3) Usuń produkt\n(4) Zmień program\n(5) Wyloguj się\n(6) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 6.")
        else:
            print("(1) Dodaj produkt\n(2) Zmień produkt\n(3) Usuń produkt\n(4) Wyloguj się\n(5) Wyjdź")
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

def is_numeric(x):
    x=str(x)
    i=1
    length=len(x)
    wasDot=0
    if ord(x[0])==45:
        pass
    elif ord(x[0]) in range (48,58):
        pass
    elif ord(x[0])==46:
        wasDot=1
    else:
        return False
    while i<length:
        if ord(x[i]) in range (48,58):
            pass
        elif ord(x[i])==46 and wasDot==0:
            wasDot=1
        else:
            return False
        i+=1
    return True

def add_product():
    print_items=("ID: ", "producent: ","nazwa: ","ryzy: ","format(cyfra): ","gramatura(liczba): ","cena: ","ilość: ")
    max_id=int(max(dt.products, key=lambda product: int(product[0]))[0])
    product=[str(max_id+1)]
    i=-1
    j=0
    err=0
    err2=0
    while True:
        if i==7:
            break
        if i==j:
            if err==0:
                print("\n\nWpisz \"w\" by wyjść.")
            elif err2==1:
                print("\n\nERROR: Wprowadź dodatnią liczbę. Wpisz \"w\" by wyjść.")
            else:
                print("\n\nERROR: Wprowadź całkowitą dodatnią liczbę. Wpisz \"w\" by wyjść.")
            inp = input(print_items[j+1])
            os.system('cls' if os.name == 'nt' else 'clear')
            if inp == "w":
                return
            elif j>1:
                try:
                    if j<6 and j!=3 and j!=4:
                        if is_numeric(inp):
                            if j==5:
                                inp=round(float(inp),2)
                        else:
                            err2=1
                            raise ValueError
                    else:
                        inp=int(inp)
                        if inp<0:
                            raise ValueError
                        elif j in [3,4]:
                            inp = str(inp)  
                except ValueError:
                    err=1
                    i=-1
                else:
                    err2=0
                    err=0
                    product.append(inp)
                    i=-1
                    j+=1
            else:
                product.append(inp)
                i=-1
                j+=1
        else:
            i+=1
            if i==4:
                print(f"format: A{product[i]}", end='')
            elif i==5:
                print(f"gramatura: {product[i]}", end='')
            else:
                print(f"{print_items[i]}{product[i]}", end='')
            if i==5:
                print("g/m",end="")
            if i==6:
                print("zł",end="")
            if i!=j:
                print(", ",end="")
    dt.products.append(product)
    dt.write_products()
    input("\n\nSUCCESS: Dodano produkt. Wprowadź enter by kontynuować...")
    os.system('cls' if os.name == 'nt' else 'clear')

def sort(products):
    err=0
    while True:
        print("1 - malejąco\n2 - rosnąco\n0 - wyjście")
        if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 0 - 2.")
        try:
            option=int(input("\ninput: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if option not in range(0,3):
                raise ValueError 
        except ValueError:
            err=1
        else:
            if option == 0:
                return products
            elif option == 1:
                
               return sorted(products, key=lambda product: int(product[0]), reverse=True)
            elif option == 2:
                return sorted(products, key=lambda product: int(product[0]))

def del_product():
    filters=[[], [], [], [], [],[]]
    products_filtered = dt.products
    err=0
    err2=0
    while True:
        ids=[]
        for product in products_filtered:
            ids.append(product[0])
            print(f"ID: {product[0]} producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł dostępność: {product[7]}")
        if not len(products_filtered):
            err2=1
        print(f"\nID - usuń produkt\nf - zmiana filtrów\ns - sortuj przez ID\n0 - wyjście")
        if err2 == 1:
            print("ERROR: Brak dostępnych produktów dla wybranych filtrów.")
            err2 = 0
        if err == 1:
            print("ERROR: Wpisano nieodpowiednią wartość.")
            err=0
        inp = input("\ninput: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if inp in ids:
            i=0
            for product in dt.products:
                if product[0] == inp:
                    del dt.products[i]
                    dt.write_products
                    return
                i+=1
        elif inp == "f":
            products_filtered, filters = orders.change_filters(products_filtered, filters)
        elif inp == "s":
            products_filtered = sort(products_filtered)
        elif inp == "0":
            return
        else:
            err=1

def print_products(products):
    if np.size(products)==0:
        return
    elif np.size(products)!=8:
        df = pd.DataFrame(data = products, columns=["ID","Producent","Nazwa","Ryzy","Format","Gramatura","Cena","Dostępność"])
    else:
        df = pd.DataFrame(data = [products[0]], columns=["ID","Producent","Nazwa","Ryzy","Format","Gramatura","Cena","Dostępność"])
        df['Format'] = 'A' + df['Format'].astype(str)
        df['Gramatura'] = df['Gramatura'].astype(str) + 'g/m'
        df['Cena'] = df['Cena'].astype(str) + 'zł'
    print(df.to_string(index=False))


def change_product():
    filters=[[], [], [], [], [],[]]
    products_filtered = dt.products
    err=0
    err2=0
    while True:
        ids=[]
        for product in products_filtered:
            ids.append(product[0])
        print_products(products_filtered)
        if not len(products_filtered):
            err2=1
        else:
            err2 = 0
        print(f"\nID - zmień produkt\nf - zmiana filtrów\ns - sortuj przez ID\n0 - wyjście")
        if err2 == 1:
            print("ERROR: Brak dostępnych produktów dla wybranych filtrów.")
        if err == 1:
            print("ERROR: Wpisano nieodpowiednią wartość.")
            err=0
        inp = input("\ninput: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if inp in ids:
            i=0
            for product in dt.products:
                if product[0] == inp:
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print_products(product)
                        print("Zmień:\n1 - producent\n2 - nazwa\n3 - ryzy\n4 - format\n5 - gramatura\n6 - cena\n7 - dostępność\n0 - wyjście\n")
                        if err == 1:
                            print("ERROR: Wprowadź cyfrę z zakresu 0 - 7")
                            err=0
                        inp = input("input: ")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"ID: {product[0]} producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł dostępność: {product[7]}")
                        if inp == "1":
                            inp2 = input("nowy producent: ")
                            dt.products[i][1]=inp2
                        elif inp == "2":
                            inp2 = input("nowa nazwa: ")
                            dt.products[i][2]=inp2
                        elif inp == "3":
                            while True:
                                if err==1:
                                    print_products(product)
                                    print()
                                    print("ERROR: Wprowadź całkowitą dodatnią liczbę.")
                                    err = 0
                                inp2 = input("nowa ilość ryz: ")
                                os.system('cls' if os.name == 'nt' else 'clear')
                                if is_numeric(inp2):
                                    if float(inp2)>0:
                                        dt.products[i][3]=str(inp2)
                                        break
                                err=1                                        
                        elif inp == "4":
                            while True:
                                if err==1:
                                    print_products(product)
                                    print()
                                    print("ERROR: Wprowadź całkowitą dodatnią liczbę.")
                                    err = 0
                                try:
                                    inp2 = int(input("nowy format(cyfrę): "))
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    if inp2<0:
                                        raise ValueError
                                except ValueError:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    err=1
                                else:
                                    dt.products[i][4]=str(inp2)
                                    break
                        elif inp == "5":
                            while True:
                                if err==1:
                                    print_products(product)
                                    print()
                                    print("ERROR: Wprowadź całkowitą dodatnią liczbę.")
                                    err = 0
                                try:
                                    inp2 = int(input("nowa gramatura(liczba): "))
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    if inp2<0:
                                        raise ValueError
                                except ValueError:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    err=1
                                else:
                                    dt.products[i][5]=str(inp2)
                                    break
                        elif inp == "6":
                            while True:
                                if err==1:
                                    print_products(product)
                                    print()
                                    print("ERROR: Wprowadź dodatnią liczbę.")
                                    err = 0
                                inp2 = input("nowa cena: ")
                                os.system('cls' if os.name == 'nt' else 'clear')
                                if is_numeric(inp2):
                                    inp2=float(inp2)
                                    if inp2>0:
                                        dt.products[i][6]=round(inp2,2)
                                        break
                                err=1       
                        elif inp == "7":
                            while True:
                                if err==1:
                                    print_products(product)
                                    print()
                                    print("ERROR: Wprowadź całkowitą dodatnią liczbę.")
                                    err = 0
                                try:
                                    inp2 = int(input("nowa dostępność: "))
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    if inp2<0:
                                        raise ValueError
                                except ValueError:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    err=1
                                else:
                                    dt.products[i][7]=inp2
                                    break
                        elif inp == "0":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break 
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            err=1
                        dt.write_products()
                    break
                i+=1
                    
        elif inp == "f":
            products_filtered, filters = orders.change_filters(products_filtered, filters)
        elif inp == "s":
            products_filtered = sort(products_filtered)
        elif inp == "0":
            return
        else:
            err=1