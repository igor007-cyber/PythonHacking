import requests as re

url = 'udemy.com'

lista = ['admin', 'login', 'css', 'search', 'api', 'painel']

for l in lista:
    check = f"https://{l}.{url}"

    try:
        r = re.get(check)
        print(f'{check} = {r.status_code}')
        print('sucesso')
        print('#########')
    except:
        print('nao deu certo')
        continue
