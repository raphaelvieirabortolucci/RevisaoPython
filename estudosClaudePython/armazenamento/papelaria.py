"""
Atividade única: Caixa da papelaria v2

Esta atividade junta tudo: input, conversão, f-strings, if/elif/else, while/for e as estruturas novas. Você refaz o caixa da aula anterior, agora guardando todos os itens.

Crie caixa2.py:

Comece com um catálogo (lista de dicionários) com pelo menos 4 produtos, cada um com nome, preco e estoque.
Em um laço, o programa pergunta o nome do produto e a quantidade. Termina quando o usuário digitar fim.
Se o nome não existir no catálogo, mostre Produto não encontrado.
Se a quantidade for maior que o estoque, mostre Estoque insuficiente (disponível: X).
Se a quantidade for menor ou igual a zero, mostre Quantidade inválida.
Se tudo estiver certo, reduza o estoque no catálogo e adicione um dicionário {"nome", "qtd", "subtotal"} a uma lista chamada carrinho.
Ao final, aplique o desconto (acima de R$ 100: 10%; acima de R$ 50: 5%; senão, nenhum) e imprima um recibo com um for e enumerate:
1. Caneta x2 ........ R$ 7.00
2. Caderno x1 ....... R$ 12.50
Subtotal: R$ 19.50
Desconto de 0%: R$ 0.00
Total a pagar: R$ 19.50
Mostre também o item mais caro do carrinho (pelo subtotal) e o estoque restante de cada produto do catálogo.
Se o carrinho estiver vazio, mostre só Nenhuma compra realizada.

Extra: use uma compreensão de lista para gerar a lista de nomes dos produtos que ficaram com estoque zero.

Mande o código aqui quando terminar. Na próxima aula veremos funções, e a atividade será organizar esse caixa em funções reutilizáveis.
"""

produtos = []
papel = {
    "nome": "papel",
    "Preço": 10.50,
    "QtdVendida": 200,
    "estoque": 20
}
produtos.append(papel)

caneta = {
    "nome": "Caneta",
    "Preço": 3.99,
    "QtdVendida": 3,
    "estoque": 12
}
produtos.append(caneta)

mochila = {
    "nome": "Mochila",
    "Preço": 80.57,
    "QtdVendida": 1,
    "estoque": 5
}
produtos.append(mochila)

lapizera = {
    "nome": "Lapizera",
    "Preço": 3.50,
    "QtdVendida": 1,
    "estoque": 2
}
produtos.append(lapizera)

grafite = {
    "nome": "Grafite",
    "Preço": 2.99,
    "QtdVendida": 20,
    "estoque": 3
}
produtos.append(grafite)
listaCompras = []
valorTotal = 0
while True:
    
    continuar = input("Continuar compras (sim/nao): ").strip().lower()

    if continuar == "nao":
        break
    for produto in produtos:
        if produto["estoque"] == 0:
            continue
        print(produto["nome"])
        print(f"Estoque: {produto["estoque"]}")
        print(f"Preço: {produto["Preço"]} R$")
    prodEscolhido = input("Digite o produto que você quer: ").lower()

    encontrado = None
    for item in produtos:
        if item["nome"].lower() == prodEscolhido.lower():
            encontrado = item
            break
    if encontrado is None:
        print("Produto não encontrado, digite corretamente")
        continue  

    try:
        qndEscolhida = int(input(f"Digite a quantidade de {encontrado['nome']} que você quer: "))
    except ValueError:
        print("Digite um número inteiro!")
        continue


    if qndEscolhida > encontrado["estoque"]:
        print("Não tem essa quantidade no estoque! ")
        continue
    elif qndEscolhida <= 0:
        print("Digite numeros acima de zero!")
        continue
    else:
        encontrado["estoque"] -= qndEscolhida
        preco = encontrado["Preço"] * qndEscolhida
        valorTotal += preco

        compra = {
            "Nome": encontrado["nome"],
            "Quantidade": qndEscolhida,
            "Preço": preco
        }

        listaCompras.append(compra)
        

    print(listaCompras)
    if valorTotal > 100:
        print("Por ter dado mais de 100 vc tera um desconto de 10 %")
        percentual = 0.10
    elif valorTotal > 50:
        percentual = 0.05
        print("Por ter dado mais de 100 vc tera um desconto de 5 %")
    else:
        percentual = 0
    desconto = valorTotal * percentual
    totalAPagar = valorTotal - desconto

    print(f"Valor total: {totalAPagar}")
    for i, compra in enumerate(listaCompras, start=1):
        print(f"{i}. {compra['Nome']} x{compra['Quantidade']} ........ R$ {compra['Preço']:.2f}")
    break
