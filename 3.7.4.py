'''
------- решение номер 1 -------
b = [0, 0]
for i in range(int(input())):
    a = input().lower().split()
    if a[0] == 'восток':
        b[0] += int(a[1])
    elif a[0] == 'запад':
        b[0] += -int(a[1])
    elif a[0] == 'север':
        b[1] += int(a[1])
    elif a[0] == 'юг':
        b[1] += -int(a[1])
for i in b:
    print(i, end = ' ')
'''

# решение номер 2

d = {'юг': 0, 'север': 0, 'запад': 0, 'восток': 0}
for i in range(int(input())):
    a = input().lower().split()
    d[a[0]] += int(a[1])
print(d['восток'] - d['запад'], d['север'] - d['юг'])
