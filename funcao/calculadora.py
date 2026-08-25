numero1 = int(input("digite um numero: "))
numero2 = int(input("digite um segundo numero: "))

def soma():
    somar = numero1 + numero2
    print(f"A soma do numero 1 com o 2 é: {somar}")

def subtracao():
    sub = numero1 - numero2
    print(f"A subtração do numero 1 com o 2 é: {sub}")

def divisao():
    divisao = numero1 / numero2
    print(f"A divisão do numero 1 com o 2 é: {divisao}")

def mult():
    multiplica = numero1 * numero2
    print(f"A multiplicação do numero 1 com o 2 é: {multiplica}")

def subtracaoI():
    subI = numero2 - numero1
    print(f"A subtração do numero 2 com o 1 é: {subI}")

def divisaoI():
    divisaoI = numero2 / numero1
    print(f"A divisão do numero 2 com o 1 é: {divisaoI}")

def multI():
    multiplicaI = numero2 * numero1
    print(f"A multiplicação do numero 2 com o 1 é: {multiplicaI}")


def mostrarResultados ():
    soma()
    subtracao()
    subtracaoI()
    divisao()
    divisaoI()
    mult()
    multI()
    return "Fim do programa"


print(mostrarResultados())
