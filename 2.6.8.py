n = int(input())
i = 1
a = []
while len(a) < n:
    for x in range(i):
        if len(a) < n:
            a.append(i)
    i += 1
for i in range(len(a)):
    print(a[i], end = ' ')

 
