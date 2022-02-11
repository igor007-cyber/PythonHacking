import sys as s
import whois11 as w
import os as o

alvo = s.argv[1]

o.system(f'ping -c1 -w2 -4 {alvo}')
print(w.whois(alvo))
