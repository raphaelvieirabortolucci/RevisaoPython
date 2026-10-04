"""
Exercício 6 — Cadastro
Crie um programa que peça:
Nome:
Idade:

Se a idade não for um número:
Idade inválida!

Se a idade for menor que 0, gere um erro usando raise.
Exemplo:
if idade < 0:    raise ValueError("Idade não pode ser negativa")


Depois use except para tratar esse erro.
"""

while True:
    try:
        nome = input("Digite a seu nome: ")
        idade = int(input("DIgite a sua idade: "))

        if idade < 0:
            raise ValueError("Idade nao pode ser menor que zero")
        break
    except ValueError:
        print("Digite os campos corretamentos")
