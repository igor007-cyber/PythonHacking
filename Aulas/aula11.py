import requests as re

url = 'udemy.com'

file = open('subs.txt')

for f in file:
    f = f.strip()
    check = f"https://{f}.{url}"

    try:
        r = re.get(check)
        print(f'{check} = {r.status_code}')
        print('sucesso')
        print('#########')
    except:
        print('nao deu certo')
        continue
