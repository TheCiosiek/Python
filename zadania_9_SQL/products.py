import data as dt
import os
import orders
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

def menu():
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
        if (dt.auth[2][0] + dt.auth[2][1] + dt.auth[2][2])>1:
            print("(1) Dodaj produkt\n(2) Zmień produkt\n(3) Usuń produkt\n(4) Zmień program\n(5) Wyloguj się\n(6) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 6.")
                err=0
        else:
            print("(1) Dodaj produkt\n(2) Zmień produkt\n(3) Usuń produkt\n(4) Wyloguj się\n(5) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 5.")
        try:
            option=int(input("\ninput: "))
            if (dt.auth[2][0] + dt.auth[2][1] + dt.auth[2][2])>1:
                if option not in range(1, 7):
                    raise ValueError
            else:
                if option not in range(1, 6):
                    raise ValueError
                elif option > 3:
                    option += 1
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
    elif ord(x[0]) in range (48, 58):
        pass
    elif ord(x[0])==46:
        wasDot=1
    else:
        return False
    while i<length:
        if ord(x[i]) in range (48, 58):
            pass
        elif ord(x[i])==46 and wasDot==0:
            wasDot=1
        else:
            return False
        i+=1
    return True

def add_product():
    DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
    conn = sqlite3.connect(DATA_PATH)
    curs = conn.cursor()

    products = curs.execute('SELECT * from products').fetchall()

    print_items=("ID: ", "producent: ","nazwa: ","ryzy: ","format(cyfra): ","gramatura(liczba): ","cena: ","ilość: ")
    max_id=int(max(products, key=lambda product: int(product[0]))[0])
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
            #Wartość j chodzi po produktach do dodania, a i chodzi po produktach do dodania 
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
            if i==5:
                print(f"gramatura: {product[i]}", end='')
            else:
                print(f"{print_items[i]}{product[i]}", end='')
            if i==5:
                print("g/m",end="")
            if i==6:
                print("zł",end="")
            if i!=j:
                print(", ",end="")
    curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Dodano produkt " + product[2]))
    # curs.execute('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (product[0], product[1], product[2], product[3], product[4], product[5], product[6], product[7]))
    curs.execute('INSERT INTO products (producer, name, reams, format, grammage, price, stock) VALUES (?, ?, ?, ?, ?, ?, ?)', ( product[1], product[2], product[3], product[4], product[5], product[6], product[7]))
    conn.commit()
    conn.close()
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
    DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
    conn = sqlite3.connect(DATA_PATH)
    curs = conn.cursor()

    products = curs.execute('SELECT * from products').fetchall()
    
    filters=[[], [], [], [], [],[]]
    products_filtered = products
    err=0
    err2=0
    while True:
        print_products(products_filtered)
        if not len(products_filtered):
            err2=1
        print(f"\nID - usuń produkt\nf - zmiana filtrów\ns - sortuj przez ID\n0 - wyjście")
        if err2 == 1:
            print("ERROR: Brak dostępnych produktów dla wybranych filtrów.")
            err2 = 0
        if err == 1:
            print("ERROR: Wpisano nieodpowiednią wartość.")
            err = 0
        inp = input("\ninput: ")
        try:
            for product in products_filtered:
                if str(product[0]) == inp:
                    raise ValueError

            os.system('cls' if os.name == 'nt' else 'clear')   
            if inp == "f":
                products_filtered, filters = orders.change_filters(products_filtered, filters)
        
            elif inp == "s":
                products_filtered = sort(products_filtered)
            
            elif inp == "0":
                conn.close()
                return
            else:
                err=1
        except ValueError:
            curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Usunięto produkt " + product[2]))
            conn.execute('DELETE FROM products WHERE id = ?', (str(product[0]),))
            conn.commit()
            conn.close()

            DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
            conn = sqlite3.connect(DATA_PATH)
            curs = conn.cursor()

            products = curs.execute('SELECT * from products').fetchall()

            products_filtered = orders.filter_list(filters, products)
            input("SUCCESS: Poprawnie usunięto produkt. Naciśnij enter by kontynuować...")
            os.system('cls' if os.name == 'nt' else 'clear')

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
    DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
    conn = sqlite3.connect(DATA_PATH)
    curs = conn.cursor()
    products_filtered = curs.execute('SELECT * from products').fetchall()

    filters=[[], [], [], [], [],[]]
    err=0
    err2=0
    while True:
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
        inp_id = input("\ninput: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        for product in products_filtered:
            if str(product[0]) == inp_id:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_products([product])
                    print()
                    print("Zmień:\n1 - producent\n2 - nazwa\n3 - ryzy\n4 - format\n5 - gramatura\n6 - cena\n7 - dostępność\n0 - wyjście\n")
                    if err == 1:
                        print("ERROR: Wprowadź cyfrę z zakresu 0 - 7")
                        err=0
                    inp = input("input: ")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_products([product])
                    if inp == "1":
                        inp2 = input("nowy producent: ")
                        curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Zmieniono producenta produktu " + product[2]))
                        conn.execute('UPDATE products SET producer = ? WHERE id = ?', (inp2, inp_id))
                    elif inp == "2":
                        inp2 = input("nowa nazwa: ")
                        curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Zmieniono nazwę produktu " + product[2]))
                        conn.execute('UPDATE products SET name = ? WHERE id = ?', (inp2, inp_id))
                    elif inp == "3":
                        while True:
                            if err==1:
                                print_products([product])
                                print("ERROR: Wprowadź całkowitą dodatnią liczbę.")
                                err = 0
                            inp2 = input("\nnowa ilość ryz: ")
                            if is_numeric(inp2):
                                if float(inp2)>0:
                                    curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Zmieno ryzy produktu " + product[2]))
                                    conn.execute('UPDATE products SET reams = ? WHERE id = ?', (str(inp2), inp_id))
                                    break
                            os.system('cls' if os.name == 'nt' else 'clear')
                            err=1                                        
                    elif inp == "4":
                        while True:
                            if err==1:
                                print_products([product])
                                print("ERROR: Wprowadź całkowitą dodatnią liczbę.")
                                err = 0
                            try:
                                inp2 = int(input("\nnowy format(cyfrę): "))
                                if inp2<0:
                                    raise ValueError
                            except ValueError:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                err=1
                            else:
                                curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Zmieniono format produktu " + product[2]))
                                conn.execute('UPDATE products SET format = ? WHERE id = ?', (str(inp2), inp_id))
                                break
                    elif inp == "5":
                        while True:
                            if err==1:
                                print_products([product])
                                print("ERROR: Wprowadź całkowitą dodatnią liczbę.")
                                err = 0
                            try:
                                inp2 = int(input("\nnowa gramatura(liczba): "))
                                if inp2<0:
                                    raise ValueError
                            except ValueError:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                err=1
                            else:
                                curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Zmieniono gramaturę produktu " + product[2]))
                                conn.execute('UPDATE products SET grammage = ? WHERE id = ?', (str(inp2), inp_id))
                                break
                    elif inp == "6":
                        while True:
                            if err==1:
                                print_products([product])
                                print("ERROR: Wprowadź dodatnią liczbę.")
                                err = 0
                            inp2 = input("\nnowa cena: ")
                            if is_numeric(inp2):
                                inp2=float(inp2)
                                if inp2>0:
                                    curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Zmieniono cenę produktu " + product[2]))
                                    conn.execute('UPDATE products SET producer = ? WHERE id = ?', (round(inp2,2), inp_id))
                                    break
                            os.system('cls' if os.name == 'nt' else 'clear')
                            err=1       
                    elif inp == "7":
                        while True:
                            if err==1:
                                print_products([product])
                                print("ERROR: Wprowadź całkowitą dodatnią liczbę.")
                                err = 0
                            try:
                                inp2 = int(input("\nnowa dostępność: "))
                                if inp2<0:
                                    raise ValueError
                            except ValueError:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                err=1
                            else:
                                curs.execute('INSERT INTO logs VALUES (?, ?, ?)', (datetime.now().strftime("%H:%M:%S %d/%m/%y"), dt.auth[1], "Zmieniono dostępność produktu " + product[2]))
                                conn.execute('UPDATE products SET stock = ? WHERE id = ?', (inp2, inp_id))
                                break
                    elif inp == "0":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break 
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        err=1
            
                    conn.commit()
                    conn.close()

                    #odświeżenie bazy danych
                    DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
                    conn = sqlite3.connect(DATA_PATH)
                    curs = conn.cursor()

                    products = curs.execute('SELECT * from products').fetchall()
                    product = curs.execute("SELECT * FROM products WHERE id=?", (inp_id,)).fetchall()[0]

                    products_filtered = orders.filter_list(filters, products)
                    input("SUCCESS: Poprawnie zmieniono produkt. Naciśnij enter by kontynuować...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                break
        # i+=1
                    
            if inp_id == "f":
                products_filtered, filters = orders.change_filters(products_filtered, filters)
            elif inp_id == "s":
                products_filtered = sort(products_filtered)
            elif inp_id == "0":
                return
            else:
                err=1
        