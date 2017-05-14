a = str(input())
b = str(input())
c = str(input())
d = str(input())

dic = {}
redic = {}

for i in range(len(a)): # создаем словари
    dic[a[i]] = b[i] # для шифровки
    redic[b[i]] = a[i] # и для дешифровки

out_c = '' # создаем строки для перешифрованных строк
out_d = ''

for i in range(len(c)):
    out_c += dic.get(c[i])

for i in range(len(d)):
    out_d += redic.get(d[i])

print(out_c)
print(out_d)
