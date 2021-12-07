import os
import datetime
import time
def choose_option():
    error=0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("(1) Utwórz użytkownika\n(2) Dodaj film\n(3) Zmodyfikuj ilość dostępnego filmu\n(4) Zobacz całą ofertę\n(5) Sprawdź dostępność filmu\n(6) Wypożycz film\n(7) Zaloguj się\n(0) Wyjdź z programu")
        try:
            if error==1:
                print("ERROR: Wprowadzono złą wartość, spróbuj jeszcze raz.")
            option=int(input("input: "))
            if option not in range(0,8):
                raise ValueError
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                return option
        except ValueError:
            error=1

def menu(movies,users):
    option=1
    is_authenticated = [False, "user"]
    while option!=0:
        option=choose_option()
        if option == 1:
            users.update(register_user(users,is_authenticated))
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
        if option == 7:
            is_authenticated=login_user(users,is_authenticated)
    return movies, users

def register_user(users, auth):
    cont="Naciśnij enter by kontynuować..."
    new_user={}
    if auth==(True,"admin"):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            password_pass={"Sześć znaków":0,"Duże litery":0,"Małe litery":0,"Cyfry":0,"Znaki specjalne":0}
            print("Login powinien mieć przynajmniej 5 znaków. Wpisz 0 by wyjść do menu.")
            new_login=input("Nowy login: ")
            if new_login=="0":
                return {}
            if users.get(new_login):
                input(f"ERROR:Rejestracja niepoprawna, login już istnieje. {cont}")
                conitnue
            if len(new_login)<5:
                input(f"ERROR:Rejestracja niepoprawna, login ma mniej niż 5 znaków. {cont}")
                continue
            break
        while True:
            is_correct=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Hasło musi mieć przynajmniej 6 znaków, jedną małą i dużą literę, cyfre oraz znak specjalny. Wpisz 0 by wyjść do menu.\nNowy login: {new_login}")
            new_password=input("Nowe hasło: ")
            if new_password=="0":
                return {}
            if len(new_password)>5:
                password_pass["Sześć znaków"]+=1
            for i in new_password:
                if i.isalpha():
                    if ord(i) in range(65,91):
                        password_pass["Duże litery"]+=1
                    else:
                        password_pass["Małe litery"]+=1
                elif i.isdigit():
                    password_pass["Cyfry"]+=1
                else:
                    password_pass["Znaki specjalne"]+=1       
            for i in password_pass:
                if password_pass[i]==0:
                    isOkay=False
                else:
                    isOkay=True
                print (f"{i}: {isOkay}")        
            if isOkay:
                input(f"ERROR: Rejestracja niepoprawna. {cont}")
            else: 
                input(f"Rejestracja poprawna. {cont}")
                new_user[new_login]=new_password
                return new_user
    else:
        input(f"Tylko admin może dodać użytkownika. {cont}")
        return {}

def add_movie(movies,auth):
    cont="Naciśnij enter by kontynuować..."
    if auth==(True,"admin"):
        new_movie={}
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Wpisz 0 by wyjść do menu.")
            movie=input("Nowy film: ")
            if movie=="0":
                return {}
            if movies.get(movie):
                input(f"ERROR:Dodanie filmu niepoprawne, film już istnieje w bazie danych. {cont}")
                continue
            break
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Wpisz 0 by wyjść do menu.\nNowy film: {movie}")
            try:
                availability=int(input("Dostępność: "))
            except ValueError():
                input(f"ERROR:Nie wprowadzono liczby. {cont}")
                continue
            if availability==0:
                return {}
            new_movie[movie]=availability
            input(f"Wprowadzenie nowego filmu poprawne. {cont}")    
            return new_movie
    else:
        input(f"Tylko admin może dodać film. {cont}")
        return {}

def modify_movie(movies,auth):
    cont="Naciśnij enter by kontynuować..."
    if auth==(True,"admin"):
        new_movie={}
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Wpisz 0 by wyjść do menu.")
            movie=input("Film: ")
            if movie==0:
                return {}
            if not movies.get(movie):
                input(f"ERROR:Zmiana dostępnośći filmu niepoprawna, film nie istnieje w bazie danych. {cont}")
                continue
            break
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Wpisz 0 by wyjść do menu.\nFilm: {movie}")
            try:
                availability=int(input("Nowa dostępność: "))
            except ValueError():
                input(f"ERROR:Nie wprowadzono liczby. {cont}")
                continue
            if availability==0:
                return {}
            new_movie[movie]=availability
            input(f"Zmiana dostępności filmu poprawna. {cont}")    
            return new_movie
    else:
        input(f"Tylko admin może zmienić dostępność. {cont}")
        return {}

def get_movies(movies):
    cont="Naciśnij enter by kontynuować..."
    for i in movies:
            print(f"Film: {i}\nDostępność: {movies[i]}")
    input(f"{cont}")
    os.system('cls' if os.name == 'nt' else 'clear')

def check_movie_availability(movies):
    cont="Naciśnij enter by kontynuować..."
    movie=input("Film: ")
    for i in movies:
        if movie.lower()==i.lower():
            input(f"Dostępność: {movies[i]}\n{cont}")    
    input(f"Film nie istnieje w bazie danych. {cont}")

def rent_movie(movies,auth):
    cont="Naciśnij enter by kontynuować..."
    if auth[0]==True:
        movie=input("Film: ")
        for i in movies:
            if movie.lower()==i.lower():
                if movies[i]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time_now = time.localtime()
                    time_now_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_now)
                    time_string_date = datetime.datetime.strptime(time_now_string,"%m/%d/%Y, %H:%M:%S")
                    time_rent = datetime.timedelta(days=14)
                    end_time = time_string_date + time_rent
                    input(f"Wypożyczono film {i} do {end_time}.\n{cont}")
                    movies[i]-=1
                    return movies  
                else:
                    input(f"Wypożyczenie niepoprawne, brak dostępności filmu. {cont}")
                    return {}
        input(f"Film nie istnieje w bazie danych. {cont}")
        return {}
    else:
        input(f"Możliwość wypożyczenia filmu tylko dla zalogowamych użytkowników. {cont}")
        return {}
def login_user(users,auth):
    cont="Naciśnij enter by kontynuować..."
    while True:
        if auth[0]==True:
            input(f"Jesteś już zalogowany. {cont}")
            return auth
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Wpisz 0, by wyjść.")
        login=input("Login: ")
        if login=="0":
            return auth
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Wpisz 0, by wyjść.\nLogin: {login}") 
        password=input("Hasło: ")
        if password=="0":
            return auth
        if users.get(login):
            if users[login]==password:
                auth=True, login
                input(f"Zalogowanie poprawne. {cont}")
                os.system('cls' if os.name == 'nt' else 'clear')
                return auth
            else:
                input(f"Nieprawidłowy login lub hasło. {cont}")
        else:
            input(f"Nieprawidłowy login lub hasło. {cont}")
    
movies = {"Harry Potter i czara ognia":1}
users = {"admin":"Haselko$1","user1":"Haslo1!"}
movies, users=menu(movies,users)

