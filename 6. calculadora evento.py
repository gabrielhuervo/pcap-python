hora = int(input("Hora de início (horas): "))
minutos = int(input("Hora de início (minutos): "))
duracao = int(input("Duração do evento (minutos): "))
minutos = minutos + duracao # encontre o total de minutos
hora = hora + minutos // 60 # encontre o número de horas contidas nos minutos e atualize a hora
minutos = minutos % 60 # ajuste os minutos para ficar no intervalo (0..59)
hora = hora % 24 # ajuste as horas para ficar no intervalo (0..23)
print(hora, ":", minutos, sep='')