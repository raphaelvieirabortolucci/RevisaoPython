"""Desafio: peça três números e mostre o maior deles, sem usar max()."""

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite segundo numero: "))
numero3 = float(input("Digite terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} é maior")

elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} é maior")

elif numero3 > numero2 and numero3 > numero1:
    print(f"{numero3} é maior")

elif numero1 == numero2 and numero1 == numero3:
    print("todos os numeros são iguais")

elif numero1 == numero2:
    print(f"O numero 1 e 2 são o mesmo")

elif numero1 == numero3:
    print(f"O numero 1 e 3 são o mesmo")

elif numero3 == numero2:
    print(f"O numero 2 e 3 são o mesmo")
    