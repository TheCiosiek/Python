dane_logowania={'Admin':'1234'}
check=0
input_login=input("Nowa nazwa użytkownika: ")
input_password=input("Nowe hasło: ")
dane_logowania[input_login]=(input_password)
while (check==0):
    login_check=input("Nazwa użytkownika: ")
    password_check=input("Hasło użytkownika: ")
    check=dane_logowania.get(login_check, 0)
    if check:
        check=(dane_logowania.get(login_check)==password_check)
        if check:
            print("Logowanie poprawne")
    if check==0:
        print("Logowanie niepoprawne, spróbuj jeszcze raz.")
