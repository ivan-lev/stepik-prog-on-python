n = int(input())
x = 0 # счетчик проходов
z = 1 # счетчик чисел
# создаём пустой список, куда будем заносить данные
a = [[0 for j in range(n)] for i in range(n)]

# пробегаем от первого значения до последнего в дозволенном диапазоне
while z <= n ** 2:
    for i in range(x, n - x, 1): # пробегаем по горизонтали
        a[x][i] = z
        z += 1
    for i in range(x + 1, n - x, 1): # пробегаем по вертикали
        a[i][n - x - 1] = z
        z += 1
    for i in range(n - x - 1, x, -1): # пробегаем обратно по горизонтали
        a[n - x - 1][i - 1] = z
        z += 1
    for i in range(n - x - 2, x, -1): # пробегаем по вертикали обратно вверх
        a[i][x] = z
        z += 1
    x += 1

# печатаем результат
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
