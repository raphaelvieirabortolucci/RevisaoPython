"""
Exercício 3 — Idade

Peça a idade do usuário.

Se ele digitar algo que não seja um número inteiro, mostre:

Idade inválida!

Se estiver correto, mostre:

Idade cadastrada com sucesso!

Use: try, except e else.
"""

while True:
    try:
        idade = int(input("Digite a sua idade: "))

    except ValueError:
        print(f"Aqui só aceitamos numeros inteiros, nada de letras ou numeros com virgula!")

    else:
        print(f"{idade} é uma idade aceita")
        break
