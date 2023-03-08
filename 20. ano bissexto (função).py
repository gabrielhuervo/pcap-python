def e_ano_bissexto(ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True

dados_teste = [1900, 2000, 2016, 1987]
resultados_esperados = [False, True, True, False]
for i in range(len(dados_teste)):
    ano = dados_teste[i]
    print(ano, "-> ", end="")
    resultado = e_ano_bissexto(ano)
    if resultado == resultados_esperados[i]:
        print("OK")
    else:
        print("Falhou")
