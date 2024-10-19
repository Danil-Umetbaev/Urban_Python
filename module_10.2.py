from threading import Thread
import time
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            enemies -= self.power
            days += 1
            time.sleep(1)
            print(f"{self.name} сражается {days} дней, осталось {enemies} воинов.")
        print(f"{self.name} одержал победу за {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
