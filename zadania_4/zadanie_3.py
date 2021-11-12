import os
def choose_option():
    run=1
    while run==1:
        print("(1) Dodaj użytkownika\n(2) Wyświetl użytkowników\n(3) Zmień hasło użytkownika\n(4) Usuń użytkownika\n(5) Wyjdź z programu")
        try:
            option=int(input("input: "))
            if option not in (1,2,3,4,5):
                raise ValueError
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                return option
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Error: Wprowadzono złą wartość, spróbuj jeszcze raz.")
def get_info_new_user():
    run=1
    while run==1:
        try:
            print("Login musi mieć przynajmniej 5, a hasło 6 znaków")
            login=input("Wpisz login: ")
            if len(login)<5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Error: Login musi mieć przynajmniej 5 znaków, ',end='')
                raise ValueError
            else:
                password=input("Wpisz hasło: ")
                if len(password)>5:
                    check_password=input("Wpisz ponownie hasło: ")
                    if password==check_password:
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Error: Hasła muszą się zgadzać, ",end='')
                        raise ValueError
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Error: Hasło musi mieć przynajmniej 6 znaków, ",end='')
                    raise ValueError
        except ValueError:
            print('rejestracja niepoprawna.')
        else:
            return login, password

def check_again():
    while True:
        try:
            run=int(input("Wprowadź (0) by wyjść do menu, bądź (1) by spróbować jeszcze raz.\ninput: "))
            if run not in (0,1):
                raise ValueError
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Error: Wprowadzono złą wartość, spróbuj jeszcze raz.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            return run

def del_user(user_data):
    run=1
    while run==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        login=input("Wprowadź nazwę użytkownika którego chcesz usunać: ")
        if user_data.get(login):
            del user_data[login]
            run=check_again()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Error: Taki użytkownik nie istnieje.")
            run=check_again()
    return

def add_user(user_data):
    run=1
    while run==1:
        login, password=get_info_new_user()
        run=user_data.get(login, 0)
        if run:
            
            print("Eror: Login już istnieje, rejestracja niepoprawna.")
            run=check_again()
        else:
            user_data[login]=password
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Rejestracja przebiegła pomyślnie.")
            run=check_again()
    return user_data

def show_users(user_data):
    num=0
    os.system('cls' if os.name == 'nt' else 'clear')
    for login in user_data:
        num+=1
        print(f"Użytkownik_{num}:\nlogin: {login}\nhasło: {user_data[login]}\n")
    if num==0:
        print("Brak użytkowników.\n")
    input("Naciśnij enter by wyjść do menu")
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def menu(user_data):
    option=0
    while option!=5:
        option=choose_option()
        if option == 1:
            user_data=add_user(user_data)
        if option == 2:
            show_users(user_data)
        if option == 3:
            user_data=change_password(user_data)
        if option == 4:
            del_user(user_data)
    input("Program zakończony, naciśnij enter by wyjść")
    return
    
def change_password(user_data):
    run=1
    while run==1:
        login=input("Wprowadź login użytkownika którego hasło chcesz zmienić: ")
        if user_data.get(login):
            wrong_password=0
            while wrong_password==0 or wrong_password==1:
                try:
                    if wrong_password==0:
                        print("Hasło musi mieć przynajmniej 6 znaków.")
                    password=input("Wprowadź nowe hasło: ")
                    if len(password)>5:
                        check_password=input("Wpisz ponownie hasło: ")
                        if password==check_password:
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            wrong_password=1
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Error: Hasła muszą się zgadzać. ")
                            raise ValueError
                    else:
                        wrong_password=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Error: Hasło musi mieć przynajmniej 6 znaków.")
                        raise ValueError
                except ValueError:
                    pass
                else:
                    user_data[login]=password
                    return user_data
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Error: Nie ma takiego użytkownika")
            run=check_again()
    return

user_data={'loginek':'haselko'}
os.system('cls' if os.name == 'nt' else 'clear')
user_data=menu(user_data)