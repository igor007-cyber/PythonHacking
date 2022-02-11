alvos = [
    {
        'ip': "198.165.165.144",
        'so': "linux",
        'ativo': True,
        'porta': [80, 20, 21]
    },
    {
        'ip': "198.165.165.145",
        'so': "windows",
        'ativo': True,
        'porta': [80, 20, 21]
    },
    {
        'ip': "198.165.165.146",
        'so': "Mac",
        'ativo': True,
        'porta': [80, 20, 21]
    }
]

test = {
    'ip': "198.165.165.146",
    'so': "Mac",
    'ativo': True,
    'porta': [80, 20, 21]
}

print(alvos[0])


for x in alvos:
    print(f"O ip: {x['ip']} roda o {x['so']}")


# ADICIONAR OU ATUALIZAR UMA CHAVE E VALOR
print(test)
test['so'] = "linux"
print(test)


# remover
del test['so']
print(test)

# ler
print(test.values())
print(test.keys())
