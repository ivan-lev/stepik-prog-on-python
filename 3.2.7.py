n = int(input())
dict = {}
for i in range(n):
    x = int(input())
    if x not in dict:   # если знаения нет в словаре - создаем и присваиваем
        dict[x] = f(x)
        print(dict[x])
    else:               # если значение есть в словаре - печатаем его
        print(dict[x])
    
# вообще хрень какая-то....
