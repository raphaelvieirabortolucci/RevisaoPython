import Produto

class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco, estoque, validade):
        super().__init__(nome, preco, estoque)    # chama o __init__ da mãe
        self.validade = validade                  # acrescenta o que é só da filha

    def __str__(self):                            # sobrescreve o método da mãe
        return f"{self.nome} (vence em {self.validade})"


leite = ProdutoPerecivel("Leite", 5.50, 20, "30/11/2026")
leite.vender(3)         # herdado de Produto, funciona sem reescrever
print(leite)            # Leite (vence em 30/11/2026)