blocos = int(input("Digite o número de blocos: "))

altura = 0
na_camada = 1
while na_camada <= blocos:
    altura += 1
    blocos -= na_camada
    na_camada += 1

print("A altura da pirâmide é:", altura)
