import sqlite3
import os

DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
conn = sqlite3.connect(DATA_PATH)
curs = conn.cursor()

# table = """ CREATE TABLE users (
#             name CHAR(50),
#             surname CHAR(50),
#             username CHAR(30),
#             password CHAR(50)
#         );"""

# table = """ CREATE TABLE users_access (
#             username CHAR(30),
#             users BOOL,
#             products BOOL,
#             orders BOOL
#         );"""

# table = """CREATE TABLE products (
#             id INT,
#             producer CHAR (50),
#             name CHAR (50),
#             reams CHAR (6),
#             format CHAR (3),
#             grammage CHAR (5),
#             price FLOAT,
#             stock INT
#         );"""

# table = """ CREATE TABLE logs (
#             date CHAR(30),
#             user CHAR(30),
#             description CHAR(100)
#         );"""

curs.execute(table)
curs.close()