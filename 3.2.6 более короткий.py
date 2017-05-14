a = input().lower().split()
d = {}

for i in a:
    d[i] = a.count(i)

for key, value in d.items():
    print(key, value)
