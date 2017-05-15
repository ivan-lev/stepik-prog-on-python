d = int(input()) # задаём кол-во записей в списке известных слов
a = [] # задаем пустое множество, где будем хранить слова
b = []
for i in range(d):
    temp = input().lower().split() # вводим энный спиисок слов
    for x in temp: # пробегаемся по каждому слову в списке
        if x not in a: # и если его нет
            a.append(x)# то добавляем в наш словарь
for i in range(int(input())): # вводим количество строк (l) на проверку
    temp = input().split()
    for x in temp:
        if (x.lower() not in a) and (x not in b):
            b.append(x)
for i in b:
    print(i)
