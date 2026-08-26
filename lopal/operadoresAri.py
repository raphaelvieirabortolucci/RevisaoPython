print("Bem-vindo ao sistema de gerenciamento de finanças pessoais!")
receita1 = float(input("digite a sua receita primeria: "))
receita2 = float(input("digite a sua receita segundaria: "))
receita3 = float(input("digite a sua receita terciaria: "))
despesa1 = float(input("digite a sua despesa primaria: "))
despesa2 = float(input("digite a sua despesa segundaria: "))
despesa3 = float(input("digite a sua despesa terciaria: "))

recitasTotal = receita1 + receita2 + receita3
despesaTotal = despesa1 + despesa2 + despesa3

total = recitasTotal - despesaTotal

percentualDes1 = despesa1 / despesaTotal
percentualDes2 = despesa2 / despesaTotal
percentualDes3 = despesa3 / despesaTotal

percentualRes1 = receita1 / recitasTotal
percentualRes2 = receita2 / recitasTotal
percentualRes3 = receita3 / recitasTotal

print(f"Sua receita total sera de {recitasTotal}")
print(f"Sua despesa total sera de {despesaTotal}")
print(f"O seu saldo final sera de {total}")
print(f"o percentual de cada despesa é {percentualDes1} %, {percentualDes2} %, {percentualDes3} %")
print(f"o percentual de cada receita é {percentualRes1} %, {percentualRes2} %, {percentualRes3} %")
