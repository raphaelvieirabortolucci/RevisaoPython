"""
1. Herança
A ideia

Herança serve para não escrever a mesma coisa duas vezes. A filha começa como uma cópia da mãe e depois você acrescenta ou muda o que for diferente.

A pergunta que identifica uma herança correta é: “a filha é um tipo da mãe?”

Um iogurte é um produto. ✅ Herança.
Um produto tem uma categoria. ❌ Isso não é herança, é um atributo (como no seu exercício).

A classe Iogurte está vazia (pass significa “nada aqui”), mas já funciona: ela tem __init__, nome, preco e mostrar(). Tudo veio da mãe.

Como o Python encontra o método

Quando você escreve y.mostrar(), o Python procura de baixo para cima:

1. Existe "mostrar" em Iogurte?   → não
2. Existe "mostrar" em Produto?   → sim! Usa este.

Se a filha tivesse o seu próprio mostrar, o Python pararia no passo 1 e usaria o dela. É isso que permite sobrescrever.

"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar(self):
        print(f"{self.nome}: R$ {self.preco}")


class Iogurte(Produto):      # <- só isso: "Iogurte herda de Produto"
    pass                     # <- e não escrevo mais nada


y = Iogurte("Iogurte natural", 6.00)
y.mostrar()                  # Iogurte natural: R$ 6.0

"""
Acrescentando o que é só da filha

Por que o super().__init__ é necessário? Como a filha escreveu o seu próprio __init__, ele substitui o da mãe, 
e não soma. Sem a linha (A), o nome e o preco nunca seriam criados:
"""
class Iogurte2(Produto):
    def __init__(self, nome, preco, validade):
        super().__init__(nome, preco)      # (A) super() significa “a classe mãe”. A linha diz: “mãe, monte a sua parte (nome e preço)”.
        self.validade = validade           # (B) Depois a filha monta só o que é dela.


x = Iogurte2("Iogurte de morango", 5.50, 25)
x.mostrar()