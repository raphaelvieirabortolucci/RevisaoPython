"""
Desconto da papelaria: peça o valor da compra.
Acima de R$ 100, aplique 10% de desconto; acima de R$ 50, 5%; caso contrário, nenhum. Mostre o valor final.
"""

preco = float(input("Digite o valor da compra: "))

if preco >= 100:
    percentual = 0.10
elif preco >= 50:
    percentual = 0.05
else:
    percentual = 0

desconto = preco * percentual
preco_final = preco - desconto

print(f"Desconto de {percentual * 100}%: R$ {desconto}")
print(f"Valor final: R$ {preco_final}")
