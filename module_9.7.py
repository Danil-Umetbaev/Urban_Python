def is_prime(func):
    def wripper(first, second, third):
        num = func(first, second, third)
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                print(f"Число {num} - составное")
                break
        else:
            print(f"Число {num} - простое")
        return num
    return wripper

@is_prime
def sum_three(first, second, third):
    return first + second + third


result = sum_three(2, 3, 6)
print(result)

result = sum_three(1, 2, 3)
print(result)