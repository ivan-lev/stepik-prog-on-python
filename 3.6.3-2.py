import requests

path = 'https://stepic.org/media/attachments/course67/3.6.3/'
name = '699991.txt'

while True: # пока не найдём нужное повторять
    fullpath = path + name # создаём полный путь к файлу
    r = requests.get(fullpath) # запрашиваем содержимое файла

    if r.text[0:2] == 'We': # если файл начинается с We
        print(r.text) # то печатаем содержимое файла
        break # и выходим
    else: # иначе файл нам не подходит и мы заносим имя, содержащееся в нём
        name = r.text # в наш новый полный путь к следующему файлу
