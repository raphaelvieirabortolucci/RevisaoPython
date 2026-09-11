try:
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        raise ValueError("Você é menor de idade!")

except ValueError as erro:
    print("Erro:", erro)

else:
    print("Cadastro permitido!")