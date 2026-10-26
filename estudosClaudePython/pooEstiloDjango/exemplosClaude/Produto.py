class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        if quantidade > self.estoque:
            raise ValueError(f"Estoque insuficiente (disponível: {self.estoque})")
        self.estoque -= quantidade
        return self.preco * quantidade

    def repor(self, quantidade):
        self.estoque += quantidade


caderno = Produto("Caderno", 18.90, 40)
total = caderno.vender(2)       # 37.8
print(caderno.estoque)          # 38