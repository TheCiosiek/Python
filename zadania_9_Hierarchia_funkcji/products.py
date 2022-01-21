def options_products():
    error=0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("(1) Dodaj zamówienie\n(2) Usuń zamówienie\n(3) Wyszukaj zamówienie\n(4) Zmień zamówienie.")
        try:
            if error==1:
                print("ERROR: Wprowadzono złą wartość, spróbuj jeszcze raz.")
            option=int(input("input: "))
            if option not in range(1,5):
                raise ValueError
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                return option
        except ValueError:
            error=1