lst = [int(i) for i in input().split()]
x = int(input())
k = 0

for i in range(len(lst)):
    if lst[i] == x:
        print(i, end = ' ')
        k = 1
if k == 0:
    print('Отсутствует')

 
