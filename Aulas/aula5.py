def check_admin(username):
    admin = 'igor@tdi'
    if admin == username:
        msg = 'é admin'
    elif username == 'ian@tdi':
        msg = 'é um usuario'
    else:
        msg = 'nao é admin'
    return f'{username} {msg}'


print(check_admin('igor@tdi'))
print(check_admin('root@tdi'))
print(check_admin('ian@tdi'))
