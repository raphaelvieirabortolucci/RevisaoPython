contador = 0

while contador <= 10: # vai realizar a contagem ate chegar a 10
    print("contagem:", contador)
    contador += 1

print("fim") # so executa o fim quando acaba a contagem

# do... while

x = 0

while True:
    print(x)
    x += 1
    if x >= 20:
        break

print("fim")