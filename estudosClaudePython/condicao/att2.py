"""Peça uma nota de 0 a 10 e mostre: Aprovado (7 ou mais), Recuperação (de 5 a 6.9) ou Reprovado."""

nota = float(input("Digite a sua nota: "))

if nota >= 7:
    print("Aprovado")

elif nota >= 5:
    print("Recuperação")

else:
    print("Reprovado")