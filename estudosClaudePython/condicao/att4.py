"""Peça um número e diga se ele é par ou ímpar (use o que você aprendeu na Aula 3)."""

numero = int(input("Digite um numero eu eu direi se ele é par ou impar: "))

if numero % 2 == 0:
    print(f"{numero} é par")

else:
    print(f"{numero} é impar")
