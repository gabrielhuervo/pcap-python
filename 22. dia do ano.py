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
    res = dias[mes - 1]
    if mes == 2 and e_ano_bissexto(ano):
        res = 29
    return res


def dia_do_ano(ano, mes, dia):
    dias = 0
    for m in range(1, mes):
        md = dias_no_mes(ano, m)
        if md is None:
            return None
        dias += md
    md = dias_no_mes(ano, mes)
    if 1 <= dia <= md:
        return dias + dia
    else:
        return None


print(dia_do_ano(2000, 12, 31))
