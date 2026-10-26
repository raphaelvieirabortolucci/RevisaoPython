from funcoes import carregarProd, salvarProd, exibirProd, buscarProd, buscarQnt, calcularDesconto, imprimirRecibo, historicoCompras, mostrarHistorico

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

    while True:
        try:
            quantidade = buscarQnt(produto)
            break

        except ValueError as erro:
            print(erro)

    produto["estoque"] -= quantidade
    preco = produto["preco"] * quantidade
    valorTotal += preco

    listaCompras.append({"Nome": produto["nome"], "Quantidade": quantidade, "Preço": preco})

    if input('Digite "fim" para terminar (Enter para continuar): ').strip().lower() == "fim":
        break       


desconto = calcularDesconto(valorTotal)
totalAPagar = valorTotal - desconto
salvarProd(produtos)

linhas = []
for i, compra in enumerate(listaCompras, start=1):
    linhas.append(f"{i}. {compra['Nome']} x{compra['Quantidade']} ........ R$ {compra['Preço']:.2f}")
linhas.append(f"Subtotal: R$ {valorTotal:.2f}")
linhas.append(f"Desconto: R$ {desconto:.2f}")
linhas.append(f"Total a pagar: R$ {totalAPagar:.2f}")
recibo = "\n".join(linhas)      # lista de linhas → UM texto

print(recibo)
imprimirRecibo(recibo)
historicoCompras(recibo)
mostrarHistorico()