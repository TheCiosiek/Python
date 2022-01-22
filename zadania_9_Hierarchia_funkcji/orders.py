import os
import data as dt

def options():
    error=0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("(1) Dodaj zamówienie\n(2) Usuń zamówienie\n(3) Historia zamówień\n(4) Zmień zamówienie\n(4) Wyloguj się\n(5) Wyjdź")
        try:
            if error==1:
                print("ERROR: Wprowadzono złą wartość, spróbuj jeszcze raz.")
            option=int(input("input: "))
            if option not in range(1,6):
                raise ValueError
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                return option
        except ValueError:
            error=1

def menu():
    dt.load_products()
    while dt.auth[0]==True:
        option = options()
        if option == 1:
            add_order()
        elif option == 2:
            del_order()
        elif option == 3:
            change_order()
        elif option == 4:
            print_orders_history()
        elif option == 5:
            dt.auth=False, "user"
        elif option == 6:
            dt.auth = None, "user"

def filter_list(products, filters):
    i=0
    for filter in filters:
        products_filtered = []
        if filter == 0:
            for product in products:
                products_filtered.append(product)
        else:
            if i==0:
                for product in products:
                    if product[0] in filter:
                        products_filtered.append(product)
            elif i==1:
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
            products = products_filtered
        i+=1
    return products

def print_available_products(products, filters):
    available_products=[[],[],[],[],[],[0]]
    empty=True
    for product in products:
        if product[0] not in available_products[0]:
            products_filtered.append(product)
            not_empty=False
        if product[1] not in available_products[1]:
            products_filtered.append(product)
            not_empty=False
        if product[2] not in available_products[2]:
            products_filtered.append(product)
            not_empty=False
        if product[3] not in available_products[3]:
            products_filtered.append(product)
            not_empty=False
        if product[4] not in available_products[4]:
            products_filtered.append(product)
            not_empty=False
    i=0
    print_filters(available_products)
    if not filters[5]:
        print("cena: przedział")
        empty == False
    return available_products, empty

def add_filters(products, filters):
    while True:
        print("Dostępne filtry:")
        available_products, empty = print_available_products(products)
        print()
        if not filters[5]:
            available_products[5]=1
        cnt=1
        print('Filtry do dodania:')
        if empty:
            input("ERROR: Brak filtrów do dodania. Wprowadź enter by kontynuować...")
            return [[],[],[],[],[],[]]
        else:
            print_out=["producent - ","nazwa - ","ryzy - ","format - ","gramatura -","cena -"]
            for i in range (6):
                if available_products[i]:
                    print(f"{print_out[i]}{i-cnt+1}")
                else:
                    cnt+=1
            if err==1:
                print(f"ERROR: Wprowadź cyfrę z przedziału {1} - {5-cnt}")
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
        while i<len(6):
            if available_products[i]:
                cnt+=1
                if cnt==option:
                    if i==0:
                        print("producent: ",end='')
                        print(", ".join(filter))
                    elif i==1:
                        print("nazwa: ",end='')
                        print(", ".join(filter))
                    elif i==2:
                        print("ryzy: ",end='')
                        print(", ".join(filter))
                    elif i==3:
                        print("format: ",end='')
                        print(", A".join(filter))
                    elif i==4:
                        print("gramatura: ",end='')
                        print("g/m, ".join(filter),end='g/m\n')

                    elif i==5:
                        inp = input("Podaj cenę: od ")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        inp2 = input(f"Podaj cenę: od {inp} do ")
                        return [[],[],[],[],[],[inp,inp2]]
                i+=1
        



def change_filters(products, filters):
    products_filtered=[]
    err=0
    while True:
        i=0
        #wyświetlenie wyfiltrowanych produktów
        for product in products:
                i+=1
                print(f"ID: {i} producent: {product[0]} nazwa: {product[1]} ryzy: {product[2]} format: A{product[3]} gramatura: {product[4]}g/m cena: {product[5]}zł")
        print_filters(filters)
        print("1 - dodaj filtr\n2 - usuń filtr\n0 - wyjdź")
        if err==1:
            print("ERROR: Wprowadź cyfrę z przedziału 1 - 2.")
        try:
            option=int(input("\ninput: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if option not in range(0,2):
                raise ValueError 
        except ValueError:
            err=1
        else:
            if option == 0:
                return products, filters
            elif option == 1:
                filters += add_filter(products,filters)
            elif option == 2:
               filters = del_filters()
            products = filter_list(products, filters)



def print_filters(filters):
    i=0
    for filter in filters:
        if filter == 0:
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
            print("format: ",end='')
            print(", A".join(filter))
        elif i==4:
            print("gramatura: ",end='')
            print("g/m, ".join(filter),end='g/m\n')
        elif i==5:
            print("cena: ",end='')
            print(" - ".join(filter),end='g/m\n')
        i+=1

def add_order():
    filters=[0, 0, 0, 0, 0]
    products_filtered=dt.products
    while True:
        i=0
        for product in products_filtered:
            i+=1
            print(f"ID: {product[0]} producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł")
        print("Filtry:")
        print_filters(filters)
        print()
        if len(products_filtered):
            print(f"f - zmiana filtrów\ns - sortuj(cena)\n1 do {i} - produkty\n0 - wyjście")
            inp = input("input: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if inp == "f":
                products_filtered, filters = change_filters(products_filtered, filters)
            elif inp == "s":
                products_filtered = sort(tmp_products)
            elif inp == "0":
                return
            else:
                pass
        else:
            print("ERROR: Brak dostępnych produktów dla wybranych filtrów. f - zmiana filtrów")
            inp = input("input: ")