import json
import os

def write_users():
    global users
    #.join konkatenacja ścieżek. .dirname to ścieżka nad folder. łączy(ścieżka_pliku.parent , wyszukiwany plik, jeśli nie ma to go tworzy)
    data_file_path =  os.path.join(os.path.dirname(__file__), "database_users.json")
    with open(data_file_path, "w") as file:
        #nie potrzebujemy indent=2, ale wtedy można plik przeczytać
        json.dump(users, file, indent=2) 

def load_users():
    global users
    data_file_path = os.path.join(os.path.dirname(__file__), "database_users.json")
    with open(data_file_path, "r") as file:
        users = json.load(file)

def write_products():
    global products
    data_file_path =  os.path.join(os.path.dirname(__file__), "database_products.json")
    with open(data_file_path, "w") as file:
        json.dump(products, file, indent=2) 

def load_products():
    global products
    data_file_path = os.path.join(os.path.dirname(__file__), "database_products.json")
    with open(data_file_path, "r") as file:
        products = json.load(file)

def write_orders():
    global orders
    data_file_path =  os.path.join(os.path.dirname(__file__), "database_orders.json")
    with open(data_file_path, "w") as file:
        json.dump(orders, file, indent=2)

def load_orders():
    global orders
    data_file_path = os.path.join(os.path.dirname(__file__), "database_orders.json")
    with open(data_file_path, "r") as file:
        orders = json.load(file)

global users, products, orders
# order={"ID":"quantity"}
#users=[["Jim", "Halpert","jimhal","Pass123!",[1,1,0]],['Pam', 'Beesly', 'pambee', '9#-D+l7~', [0, 2, 1]],['Andy', 'Bernard', 'andber', 'x`VT14$!', [0, 2, 1]],['Stanley', 'Hudson', 'stahud', '3(1D5_^9', [0, 2, 1]],['Dwight', 'Schrute', 'dwisch', 'bCB@%E$#', [0, 2, 1]],['Phyllis', 'Vance', 'phyvan', 'U38856sM', [0, 2, 1]],['Oscar', 'Martinez', 'oscmar', 'uQB9hS7_', [0, 1, 1]],['Angela', 'Martin', 'angmar', '+7=)rL7G', [0, 1, 1]],['Kevin', 'Malone', 'kevmal', '3)D1p4yW', [0, 1, 1]],['Toby', 'Flenderson', 'tobfle', '&#Zxw8Pw', [1, 0, 0]],['Darryl', 'Philbin', 'darphi', '!v2z*Z5@', [0, 1, 1]],['Lonny', 'Collins', 'loncol', ')~$Y^WG4', [0, 1, 1]],['Nate', 'Nickerson', 'natnic', 'UI5p-92B', [0, 1, 1]],['Hidetoshi', 'Hasagawa', 'hidhas', 'I)=U198r', [0, 1, 1]],['Meredith', 'Palmer', 'merpal', 'y2KR2131', [0, 1, 2]]]
# products=[["1","emerson","office paper","1","4","80",20.00,57],["2","emerson","office paper","1","4","200",35.00,37],["3","emerson","office paper","1","5","80",12.00,97],["4","emerson","office paper","1","4","200",35.00,37],["5","emerson","office paper","1","3","80",70,19],["6","emerson","office paper","5","4","80",90.00,57],["7","delux","premium","5","5","200",180.00,11]]
# write_products()
#write_users()
orders = {}
#write_orders()
auth=False, "user"

