# создаем список d[i] - класс i + 1, внутри кол-во учеников и оценка
# d = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
d = [[0, 0] for x in range(12)]
with open('dataset_3380_5.txt', 'r') as inf: # открываем файл
    for line in inf:
        line = line.strip().split('\t')
        d[int(line[0]) - 1][0] += 1 #
        d[int(line[0]) - 1][1] += int(line[2])
for i in range(11):
    if d[i][1] == 0:
        print(i + 1, '-')
    else:
        print(i + 1, d[i][1] / d[i][0])
    
