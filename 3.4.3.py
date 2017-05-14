# with open('text.txt') as inf:
#     s1 = inf.readline().lower()
s1 = []
with open('text.txt') as inf:
    line = inf.readline()
    while line:
        s1 += line.lower().split()
        line = inf.readline()

# print(s1)

d = {} # создаём пустой словарь
for i in s1: # заносим в него количество всех слов
    d[i] = s1.count(i) # где каждое уникальное слово - ключ

for key, value in d.items():
    print(key, value)

max1 = 0 # находим максимальное число повторов в словаре
for value in d.values():
    if int(value) > max1:
        max1 = int(value)

max_word = []# создаем пустой список и кидаем туда все ключи
for key, value in d.items(): # где значения равны максимуму
    if int(value) == max1:
        max_word += [key]

max_word.sort() # сортируем список

result = '' # создаём переменную с нашим слвоом и кол-м его повторений
result += str(max_word[0])
result += ' '
result += str(max1)

with open('text_out.txt', 'w') as f_out: # открываем файл для записи
    f_out.write(result)
