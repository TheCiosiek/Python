import sqlite3
import requests
import time
import json
import os
data_file_path =  os.path.join(os.path.dirname(__file__), "database_users.json")
class User:
    def __init__(self, username, password,rqst_count):
        self.username = username
        self.password = password
        self.rqst_count = rqst_count

    def update_user(self):
        self.rqst_count= int(self.rqst_count) + 1
        conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "users.db"))
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET rqst_count = {self.rqst_count} WHERE username=\'{self.username}\';')
        conn.commit()
        conn.close()
        
class Log:
    def __init__(self, username, date,type_param, number_param):
        self.username = username
        self.date = date
        self.number_param = number_param
        self.type_param = type_param
    
    def get_time():
        local_time = time.localtime()
        return time.strftime("%d/%m/%Y %H:%M:%S", local_time)

    def translate_type(inp_type):
        if inp_type == 1:
            return 'trivia'
        elif inp_type == 2:
            return "math"
        elif inp_type == 3:
            return "date"
        elif inp_type == 4:
            return "year"
        else:
            return "random"

    def add_log(self):
        conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "logs.db"))
        cursor = conn.cursor()
        cursor.execute('INSERT INTO logs VALUES (?, ?, ?, ?)', (self.username, self.date, self.type_param, self.number_param ))
        conn.commit()
        conn.close()

def check_date(string):
    numbers = string.split('/')
    if len(numbers) != 2:
        return False
    try:
        if int(numbers[0]) not in range (0,13):
            return False

        if int(numbers[1]) not in range (1,32):
            return False
    except ValueError:
        return False
    else:
        return True

def get_number(user):
    err=0
    inp_numb = None
    while True:
        try:
            inp_type=int(input("1 - trivia\n2 - math\n3 - date\n4 - year\n5 - random\ninput: "))
            if inp_type not in range (1,6):
                raise ValueError
        except ValueError:
            print("Podaj liczbę z przedziału 1 - 5.")
        else:
            while True:
                try:
                    if inp_type == 3:
                        inp_numb=input("Podaj datę w postaci xx/yy, gdzie x to miesiąc i y to dzień.\ninput: ")
                        if not check_date(inp_numb):
                            err=1
                            raise ValueError
                    elif inp_type == 5:
                        pass
                    else:
                        inp_numb = int(input("Podaj naturalną liczbę.\ninput: "))
                except ValueError:
                    if err == 1:
                        print("ERROR: Wprowadź prawidłową datę.")
                    else:
                        print("ERROR: Nie wprowadzono naturalnej liczby.")
                else:
                    break
            user.update_user()
            inp_type = Log.translate_type(inp_type)
            log = Log(user.username, Log.get_time(), inp_type, inp_numb)
            log.add_log()
            if inp_type != 'random':
                response = requests.get(f'http://numbersapi.com/{inp_numb}/{inp_type}').text
            else:
                response = requests.get(f'http://numbersapi.com/random').text
            input(f'{response}'+'\nWprowadź enter by kontynuować.')
            return

def get_logs():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "logs.db"))
    cursor = conn.cursor()
    queryset = cursor.execute('SELECT * from logs')
    logs = queryset.fetchall()
    conn.close()
    i=0
    for log in logs:
        i+=1
        print(f"log {i}:\n    użytkownik: {log[0]}, czas: {log[1]}, typ: {log[2]}, number: {log[3]}")
    input("Wprowadź enter by kontynuować...")

def get_users():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "users.db"))
    cursor = conn.cursor()
    queryset = cursor.execute('SELECT * from users')
    users = queryset.fetchall()
    conn.close()
    i=0
    for user in users:
        i+=1
        print(f"użytkownik {i}:\n    użytkownik: {user[0]}, hasło: {user[1]}, ilość zapytań: {user[2]}")
    input("Wprowadź enter by kontynuować...")

def register():
    username = input('Input username: ')
    password = input('Input password: ')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (username, password, 0))
    conn.commit()
    conn.close()

def login():
    username = input('Input username: ')
    password = input('Input password: ')
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "users.db"))
    cursor = conn.cursor()
    queryset = cursor.execute('SELECT * from users')
    users = queryset.fetchall()
    conn.close()
    user_objects = []
    for user in users:
        user_objects.append(User(user[0], user[1], user[2]))
    for user in user_objects:
        if user.username == username and user.password == password:
            return user
    return False

if __name__ == "__main__":    
    
    user = False

    while True:
        if not user:
            print('1. Zarejestruj się')
            print('2. Zaloguj się')
            print('0. Wyjdź z programu')
            option = input('Podaj opcję: ')
            if option == '1':
                register()
            elif option == '2':
                user = login()
            elif option == '0':
                break
        else:
            print('1. Wykonaj zapytanie')
            print('2. Zobacz logi')
            print('3. Zobacz uzytkowników')
            print('0. Wyjdź z programu')
            option = input('Podaj opcję: ')
            if option == '1':
                get_number(user)
            elif option == '2':
                get_logs()
            elif option == '3':
                get_users()
            elif option == '0':
                break

