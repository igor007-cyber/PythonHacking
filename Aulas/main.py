import whois11 as w


def ddos(alvo):
    return "ddos no:" + alvo


def ping(alvo):
    return "ping no:" + alvo


def nmap(alvo):
    return "nmap no:" + alvo


def whois():
    print()
    print(w.whois('tecnicasdeinvasao.com'))
