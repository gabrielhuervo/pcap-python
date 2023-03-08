income = float(input("Digite o rendimento anual: "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
    tax = 0.0

tax = round(tax, 0)
print("O imposto é:", tax, "thalers")
