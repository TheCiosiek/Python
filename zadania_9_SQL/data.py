import json
import os
import pandas as pd

# def write_users():
#     global users
#     #.join konkatenacja ścieżek. .dirname to ścieżka nad folder. łączy(ścieżka_pliku.parent , wyszukiwany plik, jeśli nie ma to go tworzy)
#     data_file_path =  os.path.join(os.path.dirname(__file__), "database_users.json")
#     with open(data_file_path, "w") as file:
#         #nie potrzebujemy indent=2, ale wtedy można plik przeczytać
#         json.dump(users, file, indent=2) 

# def load_users():
#     global users
#     data_file_path = os.path.join(os.path.dirname(__file__), "database_users.json")
#     with open(data_file_path, "r") as file:
#         users = json.load(file)

# def write_products():
#     global products
#     data_file_path =  os.path.join(os.path.dirname(__file__), "database_products.json")
#     with open(data_file_path, "w") as file:
#         json.dump(products, file, indent=2) 

# def load_products():
#     global products
#     data_file_path = os.path.join(os.path.dirname(__file__), "database_products.json")
#     with open(data_file_path, "r") as file:
#         products = json.load(file)

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
auth = False, "username", "access"