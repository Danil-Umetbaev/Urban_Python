calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, my_list):
    count_calls()
    for element in my_list:
        if element.lower() == string.lower():
            return True
    return False

print(string_info('My_name_is'))
print(string_info('Arrrgument'))
print(is_contains('UrBAN', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('rectangle', ['recycling', 'cyclic'])) # No matches
print(calls)

