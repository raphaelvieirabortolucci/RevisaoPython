"""3. Números pares

Faça um programa que mostre todos os números pares de 1 até 20 usando for. (fiz tbm com while e separei par e impar)"""

for numero in range(1, 21):
    print(numero)

numero = 1  
pares = []
impares = []

while numero <= 21:
    

    if numero % 2 == 0:
        pares.append(numero)
        numero += 1

    else:
        impares.append(numero)
        numero += 1

print(f"impares: {impares}") 
print(f"pares: {pares}")
