import json
from funcoes import carregarProd, salvarProd, exibirProd, buscarProd, buscarQnt, calcularDesconto

produtos = carregarProd()
listaCompras = []
valorTotal = 0

print("Bem vindo a minha papelaria")
while True:
    if input("Mostrar o catálogo? (sim/nao): ").strip().lower() == "sim":
        exibirProd(produtos)

    while True:
        try:
            produto = buscarProd(produtos)   
            break                            
        except ValueError as erro:           
            print(erro) 
            continue

    while True:
        try:
            quantidade = buscarQnt(produto)
            break

        except ValueError as erro:
            print(erro)

    produto["estoque"] -= quantidade
    preco = produto["Preço"] * quantidade
    valorTotal += preco

    listaCompras.append({"Nome": produto["nome"], "Quantidade": quantidade, "Preço": preco})

    if input('Digite "fim" para terminar (Enter para continuar): ').strip().lower() == "fim":
        break       

totalAPagar = valorTotal - calcularDesconto(valorTotal)
salvarProd(produto)


print(f"Valor total: {totalAPagar}")
for i, compra in enumerate(listaCompras, start=1):
    print(f"{i}. {compra['Nome']} x{compra['Quantidade']} ........ R$ {compra['Preço']:.2f}")

print(f"Subtotal: R$ {valorTotal:.2f}")
print(f"Desconto: R$ {calcularDesconto(valorTotal):.2f}")
print(f"Total a pagar: R$ {totalAPagar:.2f}") 