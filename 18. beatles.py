# Passo 1:
Beatles = []
print("Passo 1:", Beatles)

# Passo 2:
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Passo 2:", Beatles)

# Passo 3:
for membros in range(2):
    Beatles.append(input("Novo membro da banda: "))
print("Passo 3:", Beatles)

# Passo 4:
del Beatles[-1]
del Beatles[-1]
print("Passo 4:", Beatles)

# Passo 5:
Beatles.insert(0, "Ringo Starr")
print("Passo 5:", Beatles)
print("The Fab:", len(Beatles))
