my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = -1
len_list = len(my_list)
while index <= len_list:
    index += 1
    if my_list[index] == 0:
        continue
    elif my_list[index] > 0:
        print(my_list[index])
    else:
        print("Встречено отрицательное число!")
        break
