while True:
    try:
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite outro numero: "))

        resultado = numero1 / numero2

        print(f"O resultado sera: {resultado}")
        break
    except ZeroDivisionError:
        print("Não é possivel dividir por zero! ")

    except ValueError:
        print("Não pode letras! ")