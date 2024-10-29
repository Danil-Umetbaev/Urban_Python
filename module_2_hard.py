def pick_up_password(number):
    passwords = ""
    for i in range(1, first_number):
        for j in range(i + 1, first_number):
            if first_number % (i + j) == 0 and not(is_dublicate(passwords, i, j)):
                passwords += str(i) + str(j)
    return passwords

def is_dublicate(passwords, num1, num2):
    password = str(num2) + str(num1)
    for i in range(0, len(passwords)-1, 2):
        if password == passwords[i]+passwords[i+1]:
            return True
    return False

first_number = 3
while first_number <= 20:
    passwords = pick_up_password(first_number)
    print(first_number, ':', passwords)
    first_number += 1
