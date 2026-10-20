import json
from funcoes import carregarProd
from funcoes import exibirProd
from funcoes import buscarProd
from funcoes import buscarQnt
from funcoes import calcularDesconto

listaCompras = []
valor = 0
perguntar = False
print("Bem vindo a minha papelaria")
while True:
    if perguntar == True:
        print("continuar compras?")
        resposta = input('Digite "fim" para terminar as compras!').lower().strip()
        if resposta == "fim":
            break
    opcao = input("Monstrar o catalogo de produtos? (digite 'sim' para exibir a lista)"
    ":")

    if opcao == "sim":
        exibirProd(carregarProd)

    while True:
        
        buscarProd(carregarProd)
        
        if buscarProd == ValueError:
            print(ValueError)
            continue  

        else:
            break

    while True:

        
        buscarQnt(buscarProd)

        valorTotal = 0

        if buscarQnt == ValueError:
            print(ValueError)
            continue

        

        else:
            buscarProd["estoque"] -= buscarQnt
            preco = buscarProd["Preço"] * buscarQnt
            valorTotal += preco

            compra = {
                "Nome": buscarProd["nome"],
                "Quantidade": buscarQnt,
                "Preço": preco
            }

            listaCompras.append(compra)
            break
            
    continue

calcularDesconto()

totalAPagar = valorTotal - calcularDesconto

print(f"Valor total: {totalAPagar}")
for i, compra in enumerate(listaCompras, start=1):
    print(f"{i}. {compra['Nome']} x{compra['Quantidade']} ........ R$ {compra['Preço']:.2f}")

