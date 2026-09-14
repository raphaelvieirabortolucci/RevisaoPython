while True:
    try:
        numero = int(input("digite um numero: "))
        print(f"seu numero é: {numero}")
        break

    except ValueError:
        print("digite apenas numeros! ")
