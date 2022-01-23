import os
import data as dt
import operator

def options():
    err=0
    while True:
        if (bool(dt.auth[1][4][0]) + bool(dt.auth[1][4][1]) + bool(dt.auth[1][4][2]))>1:
            print("(1) Dodaj zamówienie\n(2) Usuń zamówienie\n(3) Historia zamówień\n(4) Zmień zamówienie\n(5) Zmień program\n(6) Wyloguj się\n(7) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 7.")
        else:
            print("(1) Dodaj zamówienie\n(2) Usuń zamówienie\n(3) Historia zamówień\n(4) Zmień zamówienie\n(5) Wyloguj się\n(6) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 5.")
        try:
            option=int(input("\ninput: "))
            if (bool(dt.auth[1][4][0]) + bool(dt.auth[1][4][1]) + bool(dt.auth[1][4][2]))>1:
                if option not in range(1,8):
                    raise ValueError
            else:
                if option not in range(1,6):
                    raise
                elif option >4:
                    option+=1
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            err=1
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            return option     


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
            return
        elif option == 6:
            dt.auth=False, "user"
        elif option == 7:
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

def add_filter(products, filters):
    err=0
    while True:
        print("Dostępne filtry:")
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
                print(f"ERROR: Wprowadź cyfrę z przedziału {1} - {i-cnt+2}")
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
        if available_products[i]:
            cnt+=1
            if cnt==option:
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
                            add_filters.append(inp)
                            print("SUCCESS: Dodano filtr.")
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
                            add_filters.append(inp)
                            print("SUCCESS: Dodano filtr.")
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
                            add_filters.append(inp)
                            print("SUCCESS: Dodano filtr.")
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
                print(f"ID: {product[0]} producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł dostępność: {product[7]}")
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
    # order={"ID":["quantity", "time", "status"]}
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
                    for product in products_filtered:
                        if product[0] in order:
                            i+=1
                            cost+=order[product[0]][0]*product[6]
                            print(f"pozycja {i}, ilość {order[product[0]][0]}, koszt {order[product[0]][0]*product[6]}:\n    producent: {product[1]} nazwa: {product[2]} ryzy: {product[3]} format: A{product[4]} gramatura: {product[5]}g/m cena: {product[6]}zł")
                    print(f"razem: {cost}")
                    print("\n1 - usuń pozycje\n2 - zrobić zamówienie\n0 - wyjść")
                    if err==1:
                        print("ERROR: Wprowadź cyfrę z przedziału 0 - 2.")
                    try:
                        inp=int(input("\ninput: "))
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if inp not in range(0,3):
                            raise ValueError 
                    except ValueError:
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
                                        for product in products_filtered:
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
                            pass
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
                                raise ValueError 
                        except ValueError:
                            err=1
                        else:
                            order[str(product[0])]=[inp2,"time",0]
                            input("SUCCESS: Dodano produkt do koszyka.")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break