import requests

path = 'https://stepic.org/media/attachments/course67/3.6.3/'
name = '699991.txt'

while True:
    fullpath = path + name
    r = requests.get(fullpath)
    a = r.text

    if a[0:2] == 'We':
        print(r.text)
        break
    else:
        name = r.text
#        print(name)
