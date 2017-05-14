a = [int(input())]
for i in range(a[0]):
    a += [input().split(';')]

dic = {}

for i in range(1, len(a)): # создаем словарь с названиями комманд
    for j in range(0, 3, 2):
        dic[a[i][j]] = [0,0,0,0,0]

for i in range(1, len(a)): # вносим кол-во игр каждой комманды
    for j in range(0, 3, 2):
        for key, value in dic.items():
            if a[i][j] == key:
                value[0] += 1

for i in range(1, len(a)): # производим арифметику
    if a[i][1] < a[i][3]: # если побеждает вторая команда
        temp_win = dic.get(a[i][2]) # берем их статистику из словаря
        temp_win[1] += 1 # добавляем 1 к победам
        temp_win[4] += 3 # добавляем 3 очка
        dic[a[i][2]] = temp_win # обновляем данные в словаре
        temp_los = dic.get(a[i][0]) # берем статистику проигравших
        temp_los[3] += 1 # добавляем 1 к поражениям
        dic[a[i][0]] = temp_los # обновляем статистику проигравших
    elif a[i][1] > a[i][3]: # если побеждает первая команда
        temp_win = dic.get(a[i][0]) # берем их статистику из словаря
        temp_win[1] += 1 # добавляем 1 к победам
        temp_win[4] += 3 # добавляем 3 очка
        dic[a[i][0]] = temp_win # обновляем данные в словаре
        temp_los = dic.get(a[i][2]) # берем статистику проигравших
        temp_los[3] += 1 # добавляем 1 к поражениям
        dic[a[i][2]] = temp_los # обновляем статистику проигравших
    else: # если ничья
        temp1 = dic.get(a[i][0])
        temp2 = dic.get(a[i][2])
        temp1[2] += 1 # добавляем по единице в ничьи
        temp2[2] += 1 # добавляем по 1 очку к очкам
        temp1[4] += 1 # добавляем по единице в ничьи
        temp2[4] += 1 # добавляем по 1 очку к очкам
        dic[a[i][0]] = temp1
        dic[a[i][2]] = temp2

b = ''
for key, value in dic.items():
    b += (str(key) + ':')
    for i in value:
        b += (str(i) + ' ')
    print(b)
    b = ''
# print(dic)
