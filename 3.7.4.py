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
