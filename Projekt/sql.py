import sqlite3
import os

DATA_PATH =  os.path.join(os.path.dirname(__file__), 'data.db')
conn = sqlite3.connect(DATA_PATH)
curs = conn.cursor()

# table = """CREATE TABLE "users" (
#            "name"	CHAR(50),
#            "surname"	CHAR(50),
#            "username"	CHAR(30) NOT NULL UNIQUE,
#            "password"	CHAR(50),
#            PRIMARY KEY("username")
#         );"""

# table = """ CREATE TABLE users_access (
#             username CHAR(30),
#             users BOOL,
#             products BOOL,
#             orders BOOL
#             FOREIGN KEY("username") REFERENCES "users"("username")
#         );"""

# table = """CREATE TABLE products (
#             id INTEGER UNIQUE,
#             producer CHAR (50),
#             name CHAR (50),
#             reams CHAR (6),
#             format CHAR (3),
#             grammage CHAR (5),
#             price FLOAT,
#             stock INT
#             PRIMARY KEY("id" AUTOINCREMENT)
#         );"""

# table = """ CREATE TABLE logs (
#             date CHAR(30) NOT NULL UNIQUE,
#             user CHAR(30),
#             description CHAR(100)
#             PRIMARY KEY("date")
#         );"""

curs.execute(table)
curs.close()