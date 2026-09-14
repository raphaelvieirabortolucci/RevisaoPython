"""
Exercício 4 — Conversão

Peça ao usuário um número decimal e transforme-o em float.

Se ele digitar algo inválido:

Valor inválido!

Se funcionar:

Valor aceito: 10.5
"""

while True:
    try:
        numero = int(input("digite um numero inteiro e vamos conveter para um numero com virgula: "))

    except ValueError:
        print("digite um numero inteiro, nada de letras ou numeros com virgulas")

    else:
        numeroQuebrado = numero + 0.5
        print(f"valor convertido em {numeroQuebrado}")
        break
