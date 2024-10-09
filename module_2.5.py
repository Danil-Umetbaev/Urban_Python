def get_matrix(n=0, m=0, value=0):
    matrix = list()
    if n == 0 or m == 0:
        return matrix
    for i in range(n):
        row = list()
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix


n = int(input("Введите количество строк в таблице: "))
m = int(input("Введите количество столбцов в таблице: "))
value = int(input("Введите значение, заполняющее таблицу: "))

print(get_matrix(n, m, value))
