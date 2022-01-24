def menu():
    dt.load_products()
    while dt.auth[0]==True:
        #option = options()
        #TODO
        if option == 1:
            #add_product()
            #TODO
            pass
        elif option == 2:
            #del_product()
            #TODO
            pass
        elif option == 3:
            #change_product()
            #TODO
            pass
        elif option == 4:
            return
        elif option == 6:
            dt.auth=False, "user"
        elif option == 7:
            dt.auth = None, "user"

def options():
    err=0
    while True:
        if (bool(dt.auth[1][4][0]) + bool(dt.auth[1][4][1]) + bool(dt.auth[1][4][2]))>1:
            print("(1) Dodaj produkt\n(2) Historia zamówień\n(3) Zmień zamówienie\n(4) Zmień program\n(5) Wyloguj się\n(6) Wyjdź")
            if err==1:
                print("ERROR: Wprowadź cyfrę z przedziału 1 - 6.")
        else:
            print("(1) Dodaj zamówienie\n(2) Historia zamówień\n(3) Zmień status\n(4) Wyloguj się\n(5) Wyjdź")
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

def add_product():
    #TODO
    pass

def del_product():
    #TODO
    pass

def change_product():
    #TODO
    pass