import os
def register():
    user={}
    while True:
        try:
            login=input("Wpisz login: ")
            if len(login)<6:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Login musi mieć przynajmniej 5 znaków, ',end='')
                raise ValueError
            else:
                password=input("Wpisz hasło: ")
                if len(password)>5:
                    check_password=input("Wpisz ponownie hasło: ")
                    if password==check_password:
                        user[login]=password
                        print("Rejestracja przebiegła pomyślnie")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Hasła muszą się zgadzać, ",end='')
                        raise ValueError
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Hasło musi mieć przynajmniej 6 znaków, ",end='')
                    raise ValueError
        except:
            print('rejestracja niepoprawna spróbuj jeszcze raz.')
        else:
            return user
           

os.system('cls' if os.name == 'nt' else 'clear')
dane_uzytkownikow={}
dane_uzytkownikow=register()
print(dane_uzytkownikow)