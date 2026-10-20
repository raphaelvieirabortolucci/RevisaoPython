import json

def carregarProd():

    try: 

        with open("produtos.json", "r", encoding="utf-8") as f:
            produtos = json.load(f)
            return produtos

    except FileNotFoundError:
        print("Produtos não achados, gerando produtos genericos...")
        produtos = [
            
        {
            "nome": "Caixa de lápis",
            "preco": 12.90,
            "qntVendida": 12,
            "estoque": 30
        },
        {
            "nome": "Pacote de papel sulfite",
            "preco": 28.00,
            "qntVendida": 500,
            "estoque": 35
        },
        {
            "nome": "Caderno",
            "preco": 18.90,
            "qntVendida": 1,
            "estoque": 40
        }

        ]
        with open("produtos.json", "w", encoding="utf-8") as f:
            json.dump(produtos, f, ensure_ascii=False, indent=4)
        return produtos
    except json.JSONDecodeError:
        print("Arquivo corrompido")

def exibirProd(carregarProd):
    for produto in carregarProd():
        if produto["estoque"] == 0:
            continue
        return print(f"Nome: {produto["nome"]}"), print(f"Preco: {produto["preco"]}"), print(f"Estoque: {produto["estoque"]}")

def buscarProd(carregarProd):
    prodEscolhido = input("Digite o produto que você quer: ").lower()
    for item in carregarProd:
        if item["nome"].lower() == prodEscolhido.lower():
            item
            return item
        else:
            ValueError("produto não encotrado, digite o nome corretamente")
            return ValueError

def buscarQnt(encontrado):
    quantidade = int(input("Digite a quantidade que você quer comprar: "))
    if quantidade > encontrado["estoque"]:
        print("Não tem essa quantidade no estoque! ")
        return ValueError("Valor acima do que tem disponivel")

    elif quantidade < 0:
        return ValueError("Valor invalido")

def calcularDesconto(valorTotal):

    if valorTotal > 100:
        print("Por ter dado mais de 100 vc tera um desconto de 10 %")
        percentual = 0.10
    elif valorTotal > 50:
        percentual = 0.05
        print("Por ter dado mais de 100 vc tera um desconto de 5 %")
    else:
        percentual = 0
    desconto = valorTotal * percentual
    return desconto

def altrarEstoque(buscarProd):
    with open("produtos.json", "w", encoding="utf-8") as f:
        json.dump(carregarProd - buscarProd, f, ensure_ascii=False, indent=4)


    