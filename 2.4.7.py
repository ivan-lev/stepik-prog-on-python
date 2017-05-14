a = input()
b = a[0]
count = 0

for i in range(len(a)):
    if b[-1] == a[i]:
        count += 1
    else:
        b += str(count)
        b += a[i]
        count = 1
b += str(count)
print(b)
