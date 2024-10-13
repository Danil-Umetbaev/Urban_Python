def custom_write(file_name, strings):
    f = open(file_name, 'w', encoding='utf-8')
    res = {}
    for i in range(len(strings)):
        start_byte = f.tell()
        f.write(strings[i] + '\n')

        res[(i+1, start_byte )] = strings[i]
    return res

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
