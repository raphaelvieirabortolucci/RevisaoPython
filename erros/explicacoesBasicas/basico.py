while True:
    try:
        numero = int(input("Digite um número: "))

    except ValueError:
        print("Você não digitou um número!")

    else:
        print("Número aceito:", numero)

    finally:
        print("Fim da operação.")
