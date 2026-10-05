"""Peça a idade e diga se a pessoa é menor de idade, adulta ou idosa (60 ou mais)."""
idade = int(input("Digite a sua idade: "))

if idade <= 17:
    print("Você é menor de idade!")

elif idade >= 60:
    print("Você é um velhinho fofinho")

else: 
    print("Você é um adulto")
