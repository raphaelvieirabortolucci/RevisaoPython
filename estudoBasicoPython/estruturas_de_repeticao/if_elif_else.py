pessoas = int(input("quandos pessoas moram na regiao ? "))

if 1000 <= pessoas <= 19999: #impoe uma condicao para executar o comando
    print("tem o numero de pessoas de uma vila")

elif pessoas >= 20000: #impoe outra condicao caso a anterior nao cumpra
    print("tem o numero de pessoas de uma cidade")

else: # se nenhum dos anteriores se cumprir, esse sera executado
    print("tem pouca gente morando ai")
