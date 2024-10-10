def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = ['Urban', 567.23, [True, False]]
values_dict = {'a': 'Urban', 'b': 567.23, 'c': [True, False]}

print_params(*values_list)
print_params(**values_dict)

values_list2 = ['Urban', (1, 2, 3)]

print_params(*values_list2, 42)