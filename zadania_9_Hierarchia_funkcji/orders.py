import os
import data as dt
import operator
from datetime import datetime
import numpy as np

def menu():
    dt.load_orders()
    dt.load_products()
    while dt.auth[0]==True:
        option = options()
        if option == 1:
            add_order()
        elif option == 2:
            orders_history()
        elif option == 3:
            change_order()
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
            print("(1) Dodaj zamówienie\n(2) Wyświetl zamówienia\n(3) Zmień status\n(4) Zmień program\n(5) Wyloguj się\n(6) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 6.")
        else:
            print("(1) Dodaj zamówienie\n(2) Wyświetl zamówienia\n(3) Zmień status\n(4) Wyloguj się\n(5) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 5.")
        try:
            option=int(input("\ninput: "))
            if (bool(dt.auth[1][4][0]) + bool(dt.auth[1][4][1]) + bool(dt.auth[1][4][2]))>1:
                if option not in range(1,7):
                    raise ValueError
            else:
                if option not in range(1,6):
                    raise
                elif option >3:
                    option+=1
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            return option     

def filter_orders(i,j,k,l):
    orders={}
    for order_id,order in dt.orders.items():
        if order[2] == 0 and i:
            orders[order_id]=order
        elif order[2] == 1 and j:
            orders[order_id]=order
        elif order[2] == 2 and k:
            orders[order_id]=order
        elif order[2] == 3 and l:
            orders[order_id]=order
    a_status = ["anulowane","przyjęte","wysłane","dostarczone"]
    for order_id, order in orders.items():
        i=0
        if order[2] == 0:
            status = a_status[0]
        elif order[2] == 1:
            status = a_status[1]
        elif order[2] == 2:
            status = a_status[2]
        else:
            status = a_status[3]
        print(f"numer zamówienia {order_id}, status {status}, data {order[1]}:")
        for product_id in order[0]:
            for product in dt.products:
                if product[0] == product_id:
                    i+=1
                    print(f"    pozycja {i}, ilość {order[0][product[0]]}:\n        producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł")
                    break
        i+=1
    return orders

def change_order():
    filters=[1,1,1,1]
    err=0
    while True:
        orders = filter_orders(filters[0],filters[1],filters[2],filters[3])
        print("\n1 - zmień filtry\n2 - zmień status\n0 - wyjdź")
        if err==1:
            print("ERROR: Wprowadź cyfrę z przedziału 0 - 2.")
        try:
            option=int(input("\ninput: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if option not in range(0,3):
                raise ValueError
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else:
            err=0
            if option == 0:
                return
            elif option == 1:
                print_out=("Anulowane:\n0 - nie\n1 - tak","Przyjęte\n0 - nie\n1 - tak", "Wysłane:\n0 - nie\n1 - tak", "Dostarczone:\n0 - nie\n1 - tak")
                i=0
                for item in print_out:
                    while True:
                        print(item)
                        if err==1:
                            print("ERROR: Wprowadź cyfrę z przedziału 0 - 1.")
                        try:
                            option=int(input("\ninput: "))
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if option not in range(0,2):
                                raise ValueError
                        except ValueError:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            err=1
                        else:
                            filters[i]=option
                            i+=1
                            break
            elif option == 2:
                err2=0
                cont=1
                while cont==1:
                        filter_orders(filters[0],filters[1],filters[2],filters[3])
                        if err2==1:
                            print("ERROR: Nie znaleziono numeru zamówienia. Wpisz 0 by wyjść.")
                        else:
                            print("Wpisz 0 by wyjść.")
                        try:
                            inp=int(input("\nnumer zamówienia: "))
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if inp==0:
                                break
                            elif str(inp) not in orders.keys():
                                raise ValueError
                        except ValueError:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            err2=1
                        else:
                            if orders[str(inp)][2] == 0:
                                input("ERROR: Nie można zmienić statusu anulowanego zamówienia. Wprowadź enter by wyjść...")
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break
                            if inp == 0:
                                break
                            else:
                                inp=str(inp)
                                while True:
                                    a_status=["przyjęte","wysłane","dostarczone"]
                                    if orders[inp][2] == 1:
                                        status = a_status[0]
                                    elif orders[inp][2] == 2:
                                        status = a_status[1]
                                    else:
                                        status = a_status[2]
                                    inp=str(inp)
                                    i=0
                                    print(f"numer zamówienia {inp}, status {orders[inp][2]}, data {orders[inp][1]}:")
                                    for product_id in orders[inp][0]:
                                        for product in dt.products:
                                            if product[0] == product_id:
                                                print(f"    pozycja {i}, ilość {orders[inp][0][product[0]]}:\n        producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł")
                                                i+=1
                                                break
                                    print("0 - anulowane\n1 - przyjęte\n2 - wysłane\n3 - dostarczone\nw - wyjść")
                                    if err==1:
                                        print("ERROR: Wprowadź cyfrę z przedziału 0 - 3.")
                                    try:
                                        inp2=input("\nnowy status: ")
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if inp2 == "w":
                                            pass
                                        else:
                                            inp2 = int(inp2)
                                            if inp2 not in range(0, 4):
                                                raise ValueError
                                    except ValueError:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        err=1
                                    else:
                                        if inp2=="w":
                                            cont=0
                                            break
                                        i=0
                                        for product in dt.products:
                                            if product[0] in orders[inp][0]:
                                                dt.products[i][7]+=orders[inp][0][product[0]]
                                            i+=1
                                        dt.write_products()
                                        dt.orders[inp][2]=inp2
                                        dt.write_orders()
                                        cont=0
                                        break

def orders_history():
    while True:
        filter_orders(filters[0],filters[1],filters[2],filters[3])
        if err==1:
            print("ERROR: Wprowadź cyfrę z przedziału 0 - 2. Wpisz 0 by wyjść.")
        else:
            print("Wyświetl zamówieniaL\n1 - bieżące\n2 - archiwalne.")
        try:
            inp=int(input("\ninput: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if inp==0:
                break
            elif str(inp) not in orders.keys():
                raise ValueError
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else:
            if inp == 0:
                break
            elif inp == 1:
                filter_orders(0, 1, 1, 0)
                input('Wprowadź enter by kontynuowac...')
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                filter_orders(1, 0, 0, 1)
                input('Wprowadź enter by kontynuowac...')
                os.system('cls' if os.name == 'nt' else 'clear')

def filter_list(filters):
    i=1
    products = dt.products
    for filter in filters:
        products_filtered = []
        if filter == []:
            for product in products:
                products_filtered.append(product)
        else:
            if i==1:
                for product in products:
                    if product[1] in filter:
                        products_filtered.append(product)
            elif i==2:
                for product in products:
                    if product[2] in filter:
                        products_filtered.append(product)
            elif i==3:
                for product in products:
                    if product[3] in filter:
                        products_filtered.append(product)
            elif i==4:
                for product in products:
                    if product[4] in filter:
                        products_filtered.append(product)
            elif i==5:
                for product in products:
                    if product[5] in filter:
                        products_filtered.append(product)
            elif i==6:
                for product in products:
                    if product[6]>=int(filter[0]) and product[6]<=int(filter[1]):
                        products_filtered.append(product)
            products = products_filtered
        i+=1
    return products

def print_available_products(products, filters):
    available_products = [[],[],[],[],[],[]]
    empty=True
    for product in products:
        if product[1] not in available_products[0] and product[1] not in filters[0]:
            available_products[0].append(product[1])
            empty=False
        if product[2] not in available_products[1] and product[2] not in filters[1]:
            available_products[1].append(product[2])
            empty=False
        if product[3] not in available_products[2] and product[3] not in filters[2]:
            available_products[2].append(product[3])
            empty=False
        if product[4] not in available_products[3] and product[4] not in filters[3]:
            available_products[3].append(product[4])
            empty=False
        if product[5] not in available_products[4] and product[5] not in filters[4]:
            available_products[4].append(product[5])
            empty=False
    print_filters(available_products)
    if not filters[5]:
        empty == False
    return available_products, empty

def change_filter(i, available_products):
        add_filters=[]
        if i==0:
            while True:
                s=", "
                print(f"Dostępne filtry(producent): {s.join(available_products[i])}")
                inp = input("Wpisz 0 by wyjść.\n\nwprowadź producenta: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                if inp=="0":
                    if add_filters:
                        return [add_filters,[],[],[],[],[]]
                    else:
                        return [[],[],[],[],[],[]]
                elif inp in add_filters:
                    print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                elif inp not in available_products[0]:
                    print("ERROR: Brak producenta w wybranych filtrach.")
                else:
                    print("SUCCESS")
                    add_filters.append(inp)
        elif i==1:
            while True:
                s=", "
                print(f"Dostępne filtry(nazwa): {s.join(available_products[i])}")
                inp = input("Wpisz 0 by wyjść.\n\nwprowadź nazwę: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                if inp=="0":
                    if add_filters:
                        return [[],add_filters,[],[],[],[]]
                    else:
                        return [[],[],[],[],[],[]]
                elif inp in add_filters:
                    print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                elif inp not in available_products[1]:
                    print("ERROR: Brak nazwy w dostępnych filtrach.")
                else:
                    print("SUCCESS")
                    add_filters.append(inp)
        elif i==2:
            s=", "
            while True:
                print(f"Dostępne filtry(ryzy): {s.join(available_products[i])}")
                inp = input("Wpisz 0 by wyjść.\n\nwprowadź ilość ryz: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                if inp=="0":
                    if add_filters:
                        return [[],[],add_filters,[],[],[]]
                    else:
                        return [[],[],[],[],[],[]]
                elif inp in add_filters:
                    print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                elif inp not in available_products[2]:
                    print("ERROR: Brak ryzy w dostępnych filtrach.")
                else:
                    print("SUCCESS")
                    add_filters.append(inp)
        elif i==3:
            s=", A"
            while True:
                print(f"Dostępne filtry(format): A{s.join(available_products[i])}")
                inp = input("Wpisz 0 by wyjść.\n\nwprowadź format(cyfrę): ")
                os.system('cls' if os.name == 'nt' else 'clear')
                if inp=="0":
                    if add_filters:
                        return [[],[],[],add_filters,[],[]]
                    else:
                        return [[],[],[],[],[],[]]
                elif inp in add_filters:
                    print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                elif inp not in available_products[3]:
                    print("ERROR: Brak formatu w dostępnych filtrach.")
                else:
                    print("SUCCESS")
                    add_filters.append(inp)
        elif i==4:
            s="g/m, "
            while True:
                print(f"Dostępne filtry(gramatura): {s.join(available_products[i])}",end = "g/m\n")
                inp = input("Wpisz 0 by wyjść.\n\nwprowadź gramaturę(liczba): ")
                os.system('cls' if os.name == 'nt' else 'clear')
                if inp=="0":
                    if add_filters:
                        return [[],[],[],[],add_filters,[]]
                    else:
                        return [[],[],[],[],[],[]]
                elif inp in add_filters:
                    print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                elif inp not in available_products[4]:
                    print("ERROR: Brak gramatury w dostępnych filtrach.")
                else:
                    print("SUCCESS")
                    add_filters.append(inp)
        elif i==5:
            while True:
                inp = input("Podaj cenę: od ")
                os.system('cls' if os.name == 'nt' else 'clear')
                inp2 = input(f"Podaj cenę: od {inp} do ")
                os.system('cls' if os.name == 'nt' else 'clear')
                return [[],[],[],[],[],[inp,inp2]]

def add_filters(products, filters):
    err=0
    while True:
        print("Dostępne filtry do dodania:")
        available_products, empty = print_available_products(products, filters)
        if not filters[5]:
            print("cena") 
            available_products[5]=1
        cnt=0
        print('\nFiltry do dodania:')
        if empty:
            input("ERROR: Brak filtrów do dodania. Wprowadź enter by kontynuować...")
            os.system('cls' if os.name == 'nt' else 'clear')
            return [[],[],[],[],[],[]]
        else:
            print_out=[" - producent"," - nazwa"," - ryzy"," - format"," - gramatura"," - cena"]
            for i in range (6):
                if available_products[i]:
                    print(f"{i-cnt+1}{print_out[i]}")
                else:
                    cnt+=1
            if err==1:
                print(f"ERROR: Wprowadź cyfrę z przedziału {1} - {6-cnt}")
            try:
                option = int(input("\ninput: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                if option not in range (1, i-cnt+2):
                    raise ValueError()
            except ValueError:
                err=1 
            else:
                break
    i=0
    cnt=0
    while i<6:
        if available_products[i]:
            cnt+=1
            if cnt==option:
                return_filters = change_filter(i, available_products)
                return return_filters
        i+=1

def del_filters(filters):
    err=0
    while True:
        cnt=0
        print("Dostępne filtry do usunięcia:")
        print_filters(filters)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_out=[" - producent"," - nazwa"," - ryzy"," - format"," - gramatura"," - cena"]
        for i in range (6):
            if filters[i]:
                print(f"{i-cnt+1}{print_out[i]}")
            else:
                cnt+=1
        if err==1:
            print(f"ERROR: Wprowadź cyfrę z przedziału {1} - {6-cnt}")
        try:
            option = int(input("\ninput: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if option not in range (1, i-cnt+2):
                raise ValueError()
        except ValueError:
            err=1 
        else:
            break
    i=0
    cnt=0
    add_filters=[]
    while i<6:
        if filters[i]:
            cnt+=1
            if cnt==option:
                return_filters = change_filter(i, filters)
                return return_filters
        i+=1



def change_filters(products, filters):
    products_filtered=[]
    err=0
    while True:
        i=0
        #wyświetlenie wyfiltrowanych produktów
        for product in products:
                i+=1
                print(f"ID: {product[0]} producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł dostępność: {product[7]}")
        print("Filtry:")
        print_filters(filters)
        print()
        print("1 - dodaj filtr\n2 - usuń filtr\n0 - wyjdź")
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
            os.system('cls' if os.name == 'nt' else 'clear')
            if option == 0:
                return products, filters
            elif option == 1: 
                add_elements = add_filters(products,filters)
                i=0
                while i < 6:
                    filters[i]+=add_elements[i]
                    i+=1
            elif option == 2:
                del_elements = del_filters(filters)
                i=0
                j=0
                new_filters=[]
                while i<6:
                    diff = np.setdiff1d(filters[i], del_elements[j])
                    diff = diff.tolist()
                    new_filters.append(diff)
                    i+=1
                    j+=1
                filters = new_filters
            products = filter_list(filters)


def print_filters(filters):
    i=0
    for filter in filters:
        if filter == []:
            pass
        elif i==0:
            print("producent: ",end='')
            print(", ".join(filter))
        elif i==1:
            print("nazwa: ",end='')
            print(", ".join(filter))
        elif i==2:
            print("ryzy: ",end='')
            print(", ".join(filter))
        elif i==3:
            print("format: ",end='A')
            print(", A".join(filter))
        elif i==4:
            print("gramatura: ",end='')
            print("g/m, ".join(filter),end='g/m\n')
        elif i==5:
            print("cena: ",end='')
            print(" - ".join(filter))
        i+=1

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
                
               return sorted(products, key=lambda product: product[6], reverse=True)
            elif option == 2:
                return sorted(products, key=lambda product: product[6])

def add_order():
    filters=[[], [], [], [], [],[]]
    # order={"ID":"quantity"}
    order={}
    products_filtered=dt.products
    err=0
    while True:
        i=0
        for product in products_filtered:
            i+=1
            print(f"ID: {product[0]} producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł dostępność: {product[7]}")
        print("Filtry:\n")
        print_filters(filters)
        if len(products_filtered):
            print(f"f - zmiana filtrów\ns - sortuj przez cenę\nk - pokaż koszyk\nID - dodaj produkt do koszyka\n0 - wyjście")
            if err == 1:
                print("ERROR: Wpisano nieodpowiednią wartość.")
                err=0
            inp = input("\ninput: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if inp == "f":
                products_filtered, filters = change_filters(products_filtered, filters)
            elif inp == "s":
                products_filtered = sort(products_filtered)
            elif inp == "k":
                while True:
                    i=0
                    if not order:
                        print("Brak produktów w koszyku")
                    cost=0
                    for product in dt.products:
                        if product[0] in order:
                            i+=1
                            cost+=order[product[0]]*product[6]
                            print(f"pozycja {i}, ilość {order[product[0]]}, koszt {order[product[0]]*product[6]}:\n    producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł")
                    print(f"razem: {cost}")
                    print("\n1 - usuń pozycje\n2 - zrób zamówienie\n0 - wyjść")
                    if err==1:
                        print("ERROR: Wprowadź cyfrę z przedziału 0 - 2.")
                    try:
                        inp=int(input("\ninput: "))
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if inp not in range(0,3):
                            raise ValueError 
                    except ValueError:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        err=1
                    else:
                        if inp == 0:
                            break
                        elif inp == 1:
                            while inp!="0":
                                if not order:
                                    input("ERROR: Brak dostępnych pozycji do usunięcia. Wprowadź enter by kontynuować...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break
                                else:
                                    while order:
                                        i=0
                                        for product in dt.products:
                                            if product[0] in order:
                                                i+=1
                                                print(f"pozycja {i}, ilość {order[product[0]][0]}:\n    producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł")
                                        inp = input("\nWpisz 0 by wyjść. Pozycja do usunięcia: ")
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if inp=="0":
                                            break
                                        else:
                                            i=0
                                            for product in products_filtered:
                                                if product[0] in order:
                                                    i+=1
                                                    if str(i)==inp:
                                                        del order[product[0]]

                        elif inp == 2:
                            i=1
                            for order_i in dt.orders:
                                i+=1
                            now = datetime.now()
                            dt.orders[str(i)]=[order, now.strftime("%d/%m/%y, %H:%M:%S"), 1]
                            i=0
                            while i<len(dt.products):
                                if dt.products[i][0] in order:
                                    dt.products[i][7]-=order[dt.products[i][0]]
                                i+=1
                            dt.write_products()
                            dt.write_orders()
                            order={}
                            print("SUCCES: Utworzono zamówienie.")
                            break
            elif inp == "0":
                return
            else:
                getter = operator.itemgetter(0)
                ids=map(getter, products_filtered)
                if inp not in ids:
                    err = 1
                else:
                    err=0
                    while True:
                        for product in products_filtered:
                            if product[0]==inp:
                                print(f"ID: {product[0]} producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł dostępność: {product[7]}")
                                break
                        print("ilość produktu:")
                        if err==1:
                            print(f"ERROR: Wprowadź liczbę z przedziału 0 - {product[7]} ")
                        try:
                            inp2=int(input("\ninput: "))
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if inp2 == 0:
                                break
                            elif inp2 not in range(1,(product[7]+1)):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                raise ValueError 
                        except ValueError:
                            err=1
                        else:
                            order[str(product[0])]=inp2
                            input("SUCCESS: Dodano produkt do koszyka.")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break