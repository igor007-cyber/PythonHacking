'''
numeros = [1, 2, 3, 4]

for a in numeros:
    print(a)
'''
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
        'ativo': False,
        'porta': [80, 20, 21]
    }
]


for alvo in alvos:
    if alvo['ativo']:
        print(alvo['ip'])
        for portas in alvo['porta']:
            print(f"atacando a porta: {portas}")
        print('#####')
