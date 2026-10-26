import json
from datetime import datetime
import unicodedata

def semAcento(texto):
    decomposto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in decomposto if unicodedata.category(c) != "Mn")

def carregarProd():

    try: 

        with open("produtos.json", "r", encoding="utf-8") as f:
            produtos = json.load(f)
            return produtos

    except FileNotFoundError:
        print("Produtos não achados, gerando produtos genericos...")
        produtos = [
            
        {"nome": "Caixa de lápis", "preco": 12.90, "qntVendida": 12, "estoque": 30},
        {"nome": "Pacote de papel sulfite", "preco": 28.00, "qntVendida": 500, "estoque": 35},
        {"nome": "Caderno", "preco": 18.90, "qntVendida": 1, "estoque": 40}

        ]
        salvarProd(produtos)
        return produtos
    except json.JSONDecodeError:
        print("Arquivo corrompido")
        return []

def exibirProd(produtos):             
    for produto in produtos:
        if produto["estoque"] == 0:
            continue                  
        print(f"{produto['nome']} | R$ {produto['preco']:.2f} | Estoque: {produto['estoque']}")

def buscarProd(produtos):
    nome = semAcento(input("Digite o produto que você quer: ").strip().lower())
    for item in produtos:
        if semAcento(item["nome"].lower()) == nome:
            return item

    raise ValueError("Produto não encontrado, digite o nome corretamente")  

def buscarQnt(produto):
    try:
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        raise ValueError("Digite um número inteiro")       
    if quantidade <= 0:
        raise ValueError("Digite um número maior que zero") 
    if quantidade > produto["estoque"]:
        raise ValueError(f"Estoque insuficiente (disponível: {produto['estoque']})")  # [3]
    return quantidade   

def calcularDesconto(valorTotal):

    if valorTotal > 100:
        print("Por ter dado mais de 100 vc tera um desconto de 10 %")
        percentual = 0.10
    elif valorTotal > 50:
        percentual = 0.05
        print("Por ter dado mais de 50 vc tera um desconto de 5 %")
    else:
        percentual = 0
    return valorTotal * percentual

def salvarProd(produtos):
    with open("produtos.json", "w", encoding="utf-8") as f:
        json.dump(produtos, f, ensure_ascii=False, indent=4)


def imprimirRecibo(recibo):
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M")
    with open("recibo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Recibo de compra dia: {agora}\n")
        arquivo.write(recibo)



def historicoCompras(recibo):
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M")
    with open("historico.txt", "a", encoding="utf-8") as arquivo:   # "a" cria se não existir
        arquivo.write(f"Recibo de {agora}\n")
        arquivo.write(recibo + "\n\n")

def mostrarHistorico():
    try:
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Nenhuma venda registrada.")