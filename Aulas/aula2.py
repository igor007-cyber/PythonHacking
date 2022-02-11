alvos = ["198.165.165.144", "198.165.165.145",
         "198.165.165.146", "198.165.165.147"]

# LER LISTA
print(alvos)
print()
print(alvos[0])
print()
print(alvos[0:2])

# ADD LISTA
alvos.append("outroIP")
print(alvos)
print()
[10, 20, 30].append(50)

alvos.insert(0, "inicio")
print(alvos)

print()
# REMOVER
alvos.remove("inicio")
print(alvos)
print()
# remove o ultimo elemento da lista
ultimo = alvos.pop()
print(alvos)
print()
print(ultimo)


# Como consultar uma lista
print(type(alvos))
print()
print(len(alvos))
print()
print("198.165.165.144" in alvos)


# TUBLE

portas = (80, 22, 21)
