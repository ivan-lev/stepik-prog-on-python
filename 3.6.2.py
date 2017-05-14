import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/314.txt')
print(r.text.count('\n'))
# otvet = len(a.splitlines())

# print(a)
