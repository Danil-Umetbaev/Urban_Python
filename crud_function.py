import sqlite3
from random import randint
connection = sqlite3.connect("products.db")
cursor = connection.cursor()


text1 = ("Самостоятельно находит и исправляет все баги, "
         "которые вы не заметили. Незаменимая вещь, когда уже слипаются глаза!")
text2 = "ТОЛЬКО ДЛЯ ВАС! Мы перевели всё на русский, читайте и наслаждайтесь!"
text3 = "Для самых самостоятельных и ответственных."
text4 = "Когда ничего из вышеперечисленного не помогло..."

titles = ["АНТИБАГ", "РУССКАЯ ДОКУМЕНТАЦИЯ", "БЕЗЛИМИТНЫЙ КОФЕ", "Путёвка на МАЛЬДИВЫ"]
text_list = [text1, text2, text3, text4]

cursor.execute("""
CREATE TABLE IF NOT EXISTS Products(
id INT,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
  "id"  INTEGER,
  "username"  TEXT NOT NULL,
  "email"  TEXT NOT NULL,
  "age"  INT NOT NULL,
  "balance"  INT NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
)
""")
#for i in range(4):
 #   cursor.execute(f"INSERT INTO Products VALUES ('{i+1}', '{titles[i]}', '{text_list[i]}', '{randint(159, 23974)}')")
def get_all_product():
    cursor.execute("""
    SELECT * FROM Products
    """)
    return cursor.fetchall()

def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (username, email, str(age), '1000'))
    connection.commit()

def is_included(username):
    info = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchone()
    return not (info is None)
connection.commit()
