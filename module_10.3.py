import time
from threading import Thread, Lock
import random
class Bank(Thread):
    def __init__(self, balance=0, lock=Lock()):
        super().__init__()
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for _ in range(100):
            rand = random.randint(50,500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += rand
            print(f'Пополнение:{rand}. Баланс: {self.balance}.')
            time.sleep(0.1)

    def take(self):
        for _ in range(100):
            rand = random.randint(50, 500)
            print(f'Запрос на {rand}.')
            if rand <= self.balance:
                self.balance -= rand
                print(f'Снятие:{rand}. Баланс: {self.balance}.')
            else:
                print("Запрос отклонён. Недостаточно средств")
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

