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
    i=1
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
    available_products=[[],[],[],[],[],[]]
    empty=True
    for product in products:
        if product[1] not in available_products[0]:
            available_products[0].append(product[1])
            empty=False
        if product[2] not in available_products[1]:
            available_products[1].append(product[2])
            empty=False
        if product[3] not in available_products[2]:
            available_products[2].append(product[3])
            empty=False
        if product[4] not in available_products[3]:
            available_products[3].append(product[4])
            empty=False
        if product[5] not in available_products[4]:
            available_products[4].append(product[5])
            empty=False
    print_filters(available_products)
    if not filters[5]:
        empty == False
    return available_products, empty

def add_filter(products, filters):
    err=1
    while err==1:
        err=0
        print("Dostępne filtry:")
        available_products, empty = print_available_products(products, filters)
        if not filters[5]:
            available_products[5]=1
        cnt=0
        print()
        print('Filtry do dodania:')
        if empty:
            input("ERROR: Brak filtrów do dodania. Wprowadź enter by kontynuować...")
            return [[],[],[],[],[],[]]
        else:
            print_out=[" - producent"," - nazwa"," - ryzy"," - format"," - gramatura"," - cena"]
            for i in range (6):
                if available_products[i]:
                    print(f"{i-cnt+1}{print_out[i]}")
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
                #ponieważ break wyrzuca mnie z while
                err=0
        os.system('cls' if os.name == 'nt' else 'clear')
        i=0
        cnt=0
        s=", "
        add_filters=[]
        while i<6:
            if available_products[i]:
                cnt+=1
                if cnt==option:
                    if i==0:
                        while True:
                            print(f"Dostępne filtry(dostawcy): {s.join(available_products[i])}")
                            inp = input("Wpisz 0 by wyjść.\nwprowadź producenta: ")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if inp=="0":
                                if add_filters:
                                    return [add_filters,[],[],[],[],[]]
                                else:
                                    [[],[],[],[],[],[]]
                            elif inp in add_filters:
                                print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                            elif inp not in available_products[0]:
                                print("ERROR: Brak producenta w wybranych filtrach.")
                            else:
                                add_filters.append(inp)
                                print("SUCCESS: Dodano filtr.")
                    elif i==1:
                        while True:
                            print(f"Dostępne filtry(dostawcy): {s.join(available_products[i])}")
                            inp = input("Wpisz 0 by wyjść.\nwprowadź nazwę: ")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if inp=="0":
                                if add_filters:
                                    return [[],add_filters,[],[],[],[]]
                                else:
                                    [[],[],[],[],[],[]]
                            elif inp in add_filters:
                                print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                            elif inp not in available_products[1]:
                                print("ERROR: Brak nazwy w dostępnych filtrach.")
                            else:
                                add_filters.append(inp)
                                print("SUCCESS: Dodano filtr.")
                    elif i==2:
                        while True:
                            print(f"Dostępne filtry(dostawcy): {s.join(available_products[i])}")
                            inp = input("Wpisz 0 by wyjść.\nwprowadź ilość ryz: ")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if inp=="0":
                                if add_filters:
                                    return [[],[],add_filters,[],[],[]]
                                else:
                                    [[],[],[],[],[],[]]
                            elif inp in add_filters:
                                print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                            elif inp not in available_products[2]:
                                print("ERROR: Brak ryzy w dostępnych filtrach.")
                            else:
                                add_filters.append(inp)
                                print("SUCCESS: Dodano filtr.")
                    elif i==3:
                        while True:
                            print(f"Dostępne filtry(dostawcy): {s.join(available_products[i])}")
                            inp = input("Wpisz 0 by wyjść.\nwprowadź format: ")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if inp=="0":
                                if add_filters:
                                    return [[],[],[],add_filters,[],[]]
                                else:
                                    [[],[],[],[],[],[]]
                            elif inp in add_filters:
                                print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                            elif inp not in available_products[3]:
                                print("ERROR: Brak formatu w dostępnych filtrach.")
                            else:
                                add_filters.append(inp)
                                print("SUCCESS: Dodano filtr.")
                    elif i==4:
                        while True:
                            print(f"Dostępne filtry(gramatura): {s.join(available_products[i])}")
                            inp = input("Wpisz 0 by wyjść.\nwprowadź gramaturę: ")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if inp=="0":
                                if add_filters:
                                    return [[],[],[],[],add_filters,[]]
                                else:
                                    [[],[],[],[],[],[]]
                            elif inp in add_filters:
                                print("ERROR: Filtr już znajduje się w wybranych filtrach.")
                            elif inp not in available_products[4]:
                                print("ERROR: Brak gramatury w dostępnych filtrach.")
                            else:
                                add_filters.append(inp)
                                print("SUCCESS: Dodano filtr.")
                    elif i==5:
                        inp = input("Podaj cenę: od ")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        inp2 = input(f"Podaj cenę: od {inp} do ")
                        os.system('cls' if os.name == 'nt' else 'clear')
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
                print(f"ID: {product[0]} producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł")
        print("Filtry:")
        print_filters(filters)
        print()
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
                add_elem = add_filter(products,filters)
                i=0
                while i <6:
                    filters[i]+=add_elem[i]
                    i+=1
                #filters = list(filters)
            elif option == 2:
               filters = del_filters()
            products = filter_list(products, filters)



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
            print("format: ",end='')
            print(", A".join(filter))
        elif i==4:
            print("gramatura: ",end='')
            print("g/m, ".join(filter),end='g/m\n')
        elif i==5:
            print("cena: ",end='')
            print(" - ".join(filter))
        i+=1

def add_order():
    filters=[[], [], [], [], [],[]]
    products_filtered=dt.products
    while True:
        i=0
        for product in products_filtered:
            i+=1
            print(f"ID: {product[0]} producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł")
        print("Filtry:\n")
        print_filters(filters)
        if len(products_filtered):
            print(f"f - zmiana filtrów\ns - sortuj(cena)\n1 do {i} - produkty\n0 - wyjście")
            inp = input("\ninput: ")
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