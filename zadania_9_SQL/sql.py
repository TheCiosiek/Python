import sqlite3
import os

DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
conn = sqlite3.connect(DATA_PATH)
curs = conn.cursor()

# table = """ CREATE TABLE users (
#             name CHAR(255),
#             surname CHAR(255),
#             username CHAR(255),
#             password CHAR(255)
#         );"""

table = """ CREATE TABLE users_access (
            username CHAR(255),
            users BOOL,
            products BOOL,
            orders BOOL
        );"""

# table = """CREATE TABLE products (
#             id INT,
#             producer CHAR (255),
#             name CHAR (255),
#             reams INT,
#             format char (4),
#             grammage INT,
#             price FLOAT,
#             stock INT
#         );"""

curs.execute(table)
curs.close()