import sqlite3
from random import randint
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
""")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'user{i}@mail.ru',
                    str(randint(10, 30)), str(randint(100, 2000))))

for i in range(2, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", ("500", str(i)))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60, ))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} / email: {user[1]} / Возраст: {user[2]} / Баланс: {user[3]}')
connection.commit()
connection.close()
