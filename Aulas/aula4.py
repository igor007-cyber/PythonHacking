def fazer_login(email, senha):
    print(f'email: {email} e sua senha: {senha}')


def hello(name):
    print(f'hello world {name}')


print(hello('igor'))
print(fazer_login('igor@gmail.com', 123))


def plus(n1, n2):
    return n1+n2


resultado = plus(10, 10)
print(resultado)
