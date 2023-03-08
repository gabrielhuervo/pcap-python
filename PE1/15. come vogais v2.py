palavra_sem_vogais = ""

palavra_usuario = input("Digite sua palavra: ")
palavra_usuario = palavra_usuario.upper()

for letra in palavra_usuario:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palavra_sem_vogais += letra
		
print(palavra_sem_vogais)
