a = []
i = 0
while True:
    spisok = str(input())
    if spisok == 'end':
        break
    a.append([int(i) for i in spisok.split()])
    i += 1

m = len(a) # находим кол-во строк
n = len(a[0]) # находим кол-во столбцов
b = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        summa = 0
        for di in range(-1, 2, 2): # пробегаемся по горизонтали
            ai = i + di
            if ai < 0:
                summa += a[m-1][j] #для первого элемента списка противоположным будет последний
            elif 0 <= ai < m:
                summa += a[ai][j] # перебираем средние элементы
            elif ai >= m:
                summa += a[0][j] #для песледнего элемента списка противоположным будет первый
        for dj in range(-1, 2, 2): # пробегаемся по вертикали точно также
            aj = j + dj
            if aj < 0:
                summa += a[i][n-1]
            elif 0 <= aj < n:
                summa += a[i][aj]
            elif aj >= n:
                summa += a[i][0]
        b[i][j] = summa
        
# Печатаем список b
for i in range(m):
    for j in range(n):
        print(b[i][j], end = ' ')
    print()

