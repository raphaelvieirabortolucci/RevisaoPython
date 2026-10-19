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

def buscarProd(nome):
    encontrado = None
    for item in carregarProd:
        if item["nome"].lower() == nome.lower():
            encontrado = item
            return encontrado

def buscarQnt(encontrado, quantidade):
    if quantidade > encontrado["estoque"]:
        print("Não tem essa quantidade no estoque! ")
        return "Falho"    

    elif quantidade < 0:
        return