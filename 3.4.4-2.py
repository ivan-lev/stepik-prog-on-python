# with open('text.txt') as inf:
#     s1 = inf.readline().lower()
s1 = []
count, summa, srednee = 0, 0, 0
with open('text.txt') as inf:
    for line in inf:
        line = line.strip()
        s1 += [line.split(';')] # добавляем значения в список

# print(s1)

with open('text_out.txt', 'w') as f_out: # открываем файл для записи
    for i in range(len(s1)): # ищем средний балл по студенту
        for j in range(1, len(s1[i])):
            summa += int(s1[i][j]) #
            count += 1
        srednee = summa / count # находим среднее
        f_out.write(str(srednee))
        f_out.write('\n')
        count, summa, srednee = 0, 0, 0

    for i in range(1, len(s1[i])): # ищем среднее за педмет по всем студентам
        for j in range(len(s1)): # почти как в прошлом цикле
            summa += int(s1[j][i])
            count += 1
        srednee = summa / count
        f_out.write(str(srednee))
        f_out.write(' ')
        count, summa, srednee = 0, 0, 0
