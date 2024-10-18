from threading import Thread
from datetime import datetime
import time

def write_words(word_count, file_name):
    f = open("file_name", 'w', encoding='utf-8')
    for count in range(1, word_count+1):
        f.write(f'Какое-то слово №{count}')
        time.sleep(0.1)
    f.close()
    print(f"Завершилась запись в файл {file_name}")

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(300, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
print(f'Работа обычных функций: {time_end-time_start}')

thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(300, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

time_start = datetime.now()

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()
print(f'Работа ПОТОКОВ: {time_end-time_start}')
