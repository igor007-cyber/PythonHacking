import requests as re

url = 'https://www.udemy.com/'

lista = ['admin', 'login', 'css', 'search', 'api']

for l in lista:
    check = url + l
    print(check)

    r = re.get(check)

    if r.status_code == 200:
        print(r.status_code)
        print('#########')
    else:
        continue
