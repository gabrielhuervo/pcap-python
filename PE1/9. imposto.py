renda = float(input("Digite o rendimento anual: "))

if renda < 85528:
    imposto = renda * 0.18 - 556.02
else:
    imposto = (renda - 85528) * 0.32 + 14839.02

if imposto < 0.0:
    imposto = 0.0

imposto = round(imposto, 0)
print("O imposto é:", imposto, "thalers")
