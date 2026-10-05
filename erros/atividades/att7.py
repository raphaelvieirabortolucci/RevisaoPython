"""
Exercício 7 — Número positivo
Faça um programa que peça um número inteiro.
Regras:
- Se não for inteiro → tratar ValueError.
- Se for menor que 0 → usar raise.
- Se for válido → mostrar o número.
- O programa deve continuar pedindo até receber um valor válido.
"""
while True:
    try:
        numero = int(input("Digite um numero inteiro: "))

        if numero <= 0:
            raise ValueError
            

        else:
            print(f"Numero valido: {numero}")
            break

    except ValueError:
        print("Digite apenas numeros inteiros e maiores que zero")
        continue