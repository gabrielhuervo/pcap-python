minha_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nova_lista = []
for numero in minha_lista:  # Percorre todos os números da lista original.
    if numero not in nova_lista:  # Se o número ainda não está na nova lista...
        nova_lista.append(numero)  # ...adiciona ele aqui.
minha_lista = nova_lista[:]  # Faz uma cópia da nova lista.
print("A lista com elementos únicos apenas:")
print(minha_lista)
