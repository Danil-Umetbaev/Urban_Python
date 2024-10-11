def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1 and str_number == '0':
        return 1
    if len(str_number) == 1:
        return number
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(1023450)
print(result)
