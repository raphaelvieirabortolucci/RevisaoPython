"""
Usa o while para pedir 2 números (usando variaveis), 

 depois um operador (usar if e elif e else, para definir o operador), 

 quando os valores serem escolhidos o laco pergunta se deseja sair, 

 continuar a operação ou zerar o resultado 
"""


resultadoAnterior = 0
while True:
    try:
        if resultadoAnterior == 0:
            numero1 = float(input("Digite um número: "))
        else:
            numero1 = resultadoAnterior

        numero2 = float(input("Digite outro número: "))
        operador = input("Digite um operador entre +, -, * e /: ")

    except ValueError:
        print("digite apenas numeros") 

    else:

        if operador == "+":
            resultado = numero1 + numero2

        elif operador == "-":
            resultado = numero1 - numero2

        elif operador == "*":
            resultado = numero1 * numero2

        elif operador == "/":
            resultado = numero1 / numero2

        else:
            print("operador invalido")
            continue    

        pergunta = """
        deseja continuar a calculadora? \n
        1 - sim \n
        2 - sim, mas zera o resultado \n
        3 - não

        """

        print(f"resultado: {resultado}") 
        escolha = int(input(pergunta))

        if escolha == 1:
            resultadoAnterior = resultado

            continue

        elif escolha == 2:
            resultadoAnterior = 0
            numero = 0
            continue

        elif escolha == 3:
            break

        else: 
            print("opcao errada")