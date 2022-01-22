
def choose_option_orders():
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



def menu():
    option=1
    auth = [False, "access"]
    while option!=0:
        option=choose_option()
        if option == 1:
            auth = login(users)
        if option == 2:
            movies.update(add_movie(movies,is_authenticated))
        if option == 3:
           movies.update(modify_movie(movies, is_authenticated))
        if option == 4:
            get_movies(movies)
        if option == 5:
            check_movie_availability(movies)
        if option == 6:
            movies.update(rent_movie(movies, is_authenticated))

    return movies, users