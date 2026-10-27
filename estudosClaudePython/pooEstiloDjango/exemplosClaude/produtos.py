from datetime import date


class Produto:
    """Classe MÃE (base). As filhas herdam tudo que está aqui."""

    def __init__(self, nome, preco, estoque, custo):
        self.nome = nome                  # atributo PÚBLICO: qualquer um acessa
        self.preco = preco
        self._estoque = 0                 # ENCAPSULAMENTO: "_" = uso interno, mexa pelo método/property
        self.__custo = custo              # ENCAPSULAMENTO: "__" = privado de verdade (o Python esconde o nome)
        self.estoque = estoque            # usa o setter abaixo, então a validação roda já na criação

    # ---------- ENCAPSULAMENTO: property controla o acesso ao estoque ----------
    @property
    def estoque(self):                    # LER:  produto.estoque
        return self._estoque

    @estoque.setter
    def estoque(self, valor):             # ESCREVER: produto.estoque = 10
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo")
        self._estoque = valor

    # ---------- MÉTODOS: o que o objeto SABE FAZER ----------
    def vender(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        if quantidade > self.estoque:
            raise ValueError(f"Estoque insuficiente (disponível: {self.estoque})")
        self.estoque -= quantidade        # passa pelo setter, então continua validado
        return self.calcular_preco_final() * quantidade

    def repor(self, quantidade):
        self.estoque += quantidade

    def margem(self):
        # só a PRÓPRIA classe enxerga self.__custo
        return round(self.preco - self.__custo, 2)

    # ---------- POLIMORFISMO: estes dois métodos serão SOBRESCRITOS nas filhas ----------
    def calcular_preco_final(self):
        return self.preco

    def descricao(self):
        return f"{self.nome} | R$ {self.calcular_preco_final():.2f} | Estoque: {self.estoque}"

    def __str__(self):
        return self.descricao()           # print(produto) chama __str__, que chama descricao()


class ProdutoPerecivel(Produto):
    """HERANÇA: ProdutoPerecivel É UM Produto, com validade."""

    def __init__(self, nome, preco, estoque, custo, validade):
        super().__init__(nome, preco, estoque, custo)   # HERANÇA: reaproveita o __init__ da mãe
        self.validade = validade                        # atributo NOVO, só do perecível (um objeto date)

    def dias_para_vencer(self):                         # método NOVO, só da filha
        return (self.validade - date.today()).days

    def calcular_preco_final(self):                     # POLIMORFISMO: sobrescreve o da mãe
        if self.dias_para_vencer() <= 7:
            return self.preco * 0.70                    # perto de vencer: 30% de desconto
        return self.preco

    def descricao(self):                                # POLIMORFISMO: sobrescreve e reaproveita o da mãe
        return f"{super().descricao()} | Vence em {self.dias_para_vencer()} dias"


class ProdutoLiquido(Produto):
    """HERANÇA: líquido tem volume e tipo de embalagem."""

    def __init__(self, nome, preco, estoque, custo, volume_ml, embalagem):
        super().__init__(nome, preco, estoque, custo)
        self.volume_ml = volume_ml
        self.embalagem = embalagem

    def preco_por_litro(self):                          # método NOVO, só da filha
        return self.calcular_preco_final() / (self.volume_ml / 1000)

    def descricao(self):                                # POLIMORFISMO
        return f"{super().descricao()} | {self.volume_ml} ml ({self.embalagem})"


class ProdutoCongelado(Produto):
    """HERANÇA: congelado tem temperatura e paga taxa de refrigeração."""

    TAXA_REFRIGERACAO = 0.05            # atributo de CLASSE: compartilhado por todos os congelados

    def __init__(self, nome, preco, estoque, custo, temperatura_c):
        super().__init__(nome, preco, estoque, custo)
        self.temperatura_c = temperatura_c

    def calcular_preco_final(self):                     # POLIMORFISMO: regra diferente da mãe
        return self.preco * (1 + self.TAXA_REFRIGERACAO)

    def descricao(self):                                # POLIMORFISMO
        return f"{super().descricao()} | Conservar a {self.temperatura_c}°C"