def e_ano_bissexto(ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True

def dias_no_mes(ano, mes):
    if ano < 1582 or mes < 1 or mes > 12:
        return None
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = dias[mes - 1]
    if mes == 2 and e_ano_bissexto(ano):
        res = 29
    return res

anos_teste = [1900, 2000, 2016, 1987]
meses_teste = [2, 2, 1, 11]
resultados_esperados = [28, 29, 31, 30]

for i in range(len(anos_teste)):
    ano = anos_teste[i]
    mes = meses_teste[i]
    print(ano, mes, "-> ", end="")
    resultado = dias_no_mes(ano, mes)
    if resultado == resultados_esperados[i]:
        print("OK")
    else:
        print("Falhou")
