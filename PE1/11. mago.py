numero_secreto = 777

print(
"""
+================================+
| Bem-vindo ao meu jogo, trouxa! |
| Digite um número inteiro       |
| e adivinhe qual número eu      |
| escolhi para você.             |
| Então, qual é o número secreto?|
+================================+
""")

numero_usuario = int(input("Digite o número: "))

while numero_usuario != numero_secreto:
    print("Ha ha! Você está preso no meu loop!")
    numero_usuario = int(input("Digite o número novamente: "))
print(numero_secreto, "Muito bem, trouxa! Agora você está livre.")
