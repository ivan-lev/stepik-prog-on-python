a = [int(i) for i in input().split()]
a.sort()
b = []
count = 0
for i in range(1,(len(a))):
    if len(a) == 1:
        break
    else:
        if a[i] == a[i - 1] and count == 0:
            b.append(a[i])
            count += 1
        elif a[i] == a[i - 1] and count == 1:
            continue
        else:
            count = 0
for i in range(len(b)):
    print(b[i], end = ' ')
