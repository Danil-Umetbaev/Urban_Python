import multiprocessing
from datetime import datetime
def read_info(file_name):
    all_data = []
    with open(file_name, 'r') as file:
        for line in file:
            all_data.append(line)

file_names = [f"./files/file {i}.txt" for i in range(1,5)]

if __name__ == "__main__":
    start = datetime.now()

    for file_name in file_names:
        read_info(file_name)
    end = datetime.now()

    res = (end - start).total_seconds()
    print(f'Линейное выполнение заняло {res} сек.')
    start = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)

    end = datetime.now()
    res = (end - start).total_seconds()
    print(f'МНОГОПРОЦЕССОРНОЕ выполнение заняло {res} сек.')