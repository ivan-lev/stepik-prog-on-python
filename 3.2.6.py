a = input().lower().split()
print('Печатаем нашу строку')
print(a)

d = {}

for i in range(len(a)):
    if a[i] in d:
        value = d.get(a[i]) + 1
        d[a[i]] = value
    else:
        d[a[i]] = 1

for key, value in d.items():
    print(key, value, end = ' ')
    print()
