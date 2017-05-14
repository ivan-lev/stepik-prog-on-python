with open('dataset_3363_2.txt', 'r') as inf: # открываем файл
    s_in = inf.readline().strip() # считываем строку
s_out = s_in[0] #записываем в выходную строку первое число
count = '' #обнуляем счетчик
for i in range(1,len(s_in)): # пробегаемся по строке со 2го символа
    s_temp = s_in[i] # берем каждый символ в отдельную переменную
    if s_temp[0].isdigit(): # если она число, то записываем её в счетчик
        count += s_temp[0]
        if i == len(s_in) - 1: # если дошли до конца строки, не забываем
            s_out += s_out[-1] * (int(count) - 1) # умножать последнюю букву
        continue # если число больше 9, то повторяем процедуру, пропуская код ниже
    elif s_temp[0].isalpha(): # если же мы наткнулись на букву, 
        s_out += s_out[-1] * (int(count) - 1)
        s_out += s_in[i]
        count = ''

with open('text_out.txt', 'w') as f_out: # открываем файл для записи
    f_out.write(s_out)
